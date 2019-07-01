<!--
  描述：拖放地图组件，默认尺寸是 500 * 300

  接收属性参数：
    lat: 纬度
    lng: 经度

  自定义事件：
    drag: 拖放完成事件

  示例：
    <mapDrag @drag="dragMap" lat="22.574405" lng="114.095388"></mapDrag>
-->
<template>
  <div class="m-map">
    <div class="search" v-if="placeSearch">
      <input type="text" placeholder="请输入关键字" v-model="searchKey">
      <button type="button" @click="handleSearch">搜索</button>
      <h2>{{sayHello()}}</h2>
      <h2>{{ message}}</h2> 
      <h2><button @click="add()">add</button></h2> 
      <div id="js-result" v-show="searchKey" class="result"></div>      
    </div>
    <div id="js-container" class="map">正在加载数据 ...</div>    
  </div>
</template>

<script>
import remoteLoad from '@/utils/remoteLoad.js'
import { MapKey, MapCityName } from '@/config/config'
export default {
//  props: ['lat', 'lng'],
  props: {message:String},
  data () {
    return {
      searchKey: '',
      placeSearch: null,
      dragStatus: false,
      AMapUI: null,
      AMap: null,
      map: null,
      mapConfig: null,
      num:'test',
      test:'test',
      a:'test',
    }
  },
  watch: {
    searchKey () {
      if (this.searchKey === '') {
        this.placeSearch.clear()
      }
      this.a++
    }
  },

  mounted: function () {
        this.$nextTick(function () {
            setInterval(this.timer, 10000);
        })
  },

  methods: {
     sayHello(){
        return this.test;
     },

    add:function(){
          this.a=this.message;
          this.test=this.message;
     },

     timer:function () {

  var marker = new AMap.Marker({
        position: new AMap.LngLat(121,31),
        icon: '//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png',
        offset: new AMap.Pixel(-13, -30)
    });

    marker.setMap(this.map);

    // 设置鼠标划过点标记显示的文字提示
    marker.setTitle('我是marker的title');

    // 设置label标签
    // label默认蓝框白底左上角显示，样式className为：amap-marker-label
    marker.setLabel({
        offset: new AMap.Pixel(20, 20),  //设置文本标注偏移量
        content: "10",
        direction: 'right' //设置文本标注方位
    });

    }, 
    handleSearch () {
      if (this.searchKey) {
        this.placeSearch.search(this.searchKey)
      }
    },
    // 实例化地图
    initMap () {
   // 加载PositionPicker，loadUI的路径参数为模块名中 'ui/' 之后的部分
      let AMapUI = this.AMapUI = window.AMapUI 
      let AMap = this.AMap = window.AMap 

      AMapUI.loadUI(['misc/PositionPicker'], PositionPicker => {
        this.mapConfig = {
          zoom: 3,
          cityName: MapCityName,
          center: [107, 33]
        }
        if (this.lat && this.lng) {
              mapConfig.center = [this.lng, this.lat]
 //           this.mapConfig.center = [102, 33]
        }
        
        this.map = new AMap.Map('js-container', this.mapConfig) 

        // 加载地图搜索插件
        AMap.service('AMap.PlaceSearch', () => {
          this.placeSearch = new AMap.PlaceSearch({
            pageSize: 1,
            pageIndex: 1,
            citylimit: true,
            city: MapCityName,
            map: this.map,
            //panel: 'js-result'
          })
        })
        // 启用工具条
        AMap.plugin(['AMap.ToolBar'], function () {
          map.addControl(new AMap.ToolBar({
            position: 'RB'
          }))
        })
        // 创建地图拖拽
        let positionPicker = new PositionPicker({
          mode: 'dragMap', // 设定为拖拽地图模式，可选'dragMap'、'dragMarker'，默认为'dragMap'
          map: this.map // 依赖地图对象
        })
        // 拖拽完成发送自定义 drag 事件
        positionPicker.on('success', positionResult => {
          // 过滤掉初始化地图后的第一次默认拖放
          if (!this.dragStatus) {
            this.dragStatus = true
          } else {
            this.$emit('drag', positionResult)
          }
        })
        // 启动拖放
        positionPicker.start()
      })
    }
  },

  async created () {

//   alert("this is test2")
 //   setTimeout(()=>{alert("this is test2")},100)

    // 已载入高德地图API，则直接初始化地图
    if (window.AMap && window.AMapUI) {
      this.initMap()
    // 未载入高德地图API，则先载入API再初始化
    } else {
      await remoteLoad(`http://webapi.amap.com/maps?v=1.3&key=${MapKey}`)
      await remoteLoad('http://webapi.amap.com/ui/1.0/main.js')
      this.initMap()
    }
  }
}
</script>

<style lang="css">
.m-map{ min-width: 500px; min-height: 300px; position: relative; }
.m-map .map{ width: 100%; height: 100%; }
.amap-icon img {width: 25px;height: 34px;}
.m-map .search{ position: absolute; top: 10px; left: 10px; width: 285px; z-index: 1; }
.m-map .search input{ width: 180px; border: 1px solid #ccc; line-height: 20px; padding: 5px; outline: none; }
.m-map .search button{ line-height: 26px; background: #fff; border: 1px solid #ccc; width: 50px; text-align: center; }
.m-map .result{ max-height: 300px; overflow: auto; margin-top: 10px; }
</style>
