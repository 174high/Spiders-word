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
            setInterval(this.timer, 3000);
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

     var provinces = [{
	"name": "北京市",
	"center": "116.405285,39.904989",
	"type": 0,
	"subDistricts": [] ,
        "elevators": 1235 ,
        }, {
	"name": "天津市",
	"center": "117.190182,39.125596",
	"type": 0,
	"subDistricts": [],
        "elevators": 3564 ,        
        }, {
	"name": "河北省",
	"center": "114.502461,38.045474",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "山西省",
	"center": "112.549248,37.857014",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "内蒙古自治区",
	"center": "111.670801,40.818311",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "辽宁省",
	"center": "123.429096,41.796767",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "吉林省",
	"center": "125.3245,43.886841",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "黑龙江省",
	"center": "126.642464,45.756967",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "上海市",
	"center": "121.472644,31.231706",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "江苏省",
	"center": "118.767413,32.041544",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "浙江省",
	"center": "120.153576,30.287459",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "安徽省",
	"center": "117.283042,31.86119",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "福建省",
	"center": "119.306239,26.075302",
	"type": 1,
	"subDistricts": [],
        "elevators": 209 , 
        }, {
	"name": "江西省",
	"center": "115.892151,28.676493",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "山东省",
	"center": "117.000923,36.675807",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "河南省",
	"center": "113.665412,34.757975",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "湖北省",
	"center": "114.298572,30.584355",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "湖南省",
	"center": "112.982279,28.19409",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "广东省",
	"center": "113.280637,23.125178",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "广西壮族自治区",
	"center": "108.320004,22.82402",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "海南省",
	"center": "110.33119,20.031971",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "重庆市",
	"center": "106.504962,29.533155",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "四川省",
	"center": "104.065735,30.659462",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "贵州省",
	"center": "106.713478,26.578343",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "云南省",
	"center": "102.712251,25.040609",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "西藏自治区",
	"center": "91.132212,29.660361",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "陕西省",
	"center": "108.948024,34.263161",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "甘肃省",
	"center": "103.823557,36.058039",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "青海省",
	"center": "101.778916,36.623178",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "宁夏回族自治区",
	"center": "106.278179,38.46637",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "新疆维吾尔自治区",
	"center": "87.617733,43.792818",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "台湾省",
	"center": "121.509062,25.044332",
	"type": 2,
	"subDistricts": []
        }, {
	"name": "香港特別行政區",
	"center": "114.173355,22.320048",
	"type": 1,
	"subDistricts": []
        }, {
	"name": "澳門特別行政區",
	"center": "113.54909,22.198951",
	"type": 1,
	"subDistricts": []
        }];

        for (var i = 0; i < provinces.length; i += 1) {  
        //    if (provinces[i].type === 0) {

            if(provinces[i].elevators==null)
            continue;

            var marker = new AMap.Marker({
            position: provinces[i].center.split(','),
            icon: '//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png',
            offset: new AMap.Pixel(-12,-12),
            title: provinces[i].name,
            });

            marker.setMap(this.map);
            // 设置label标签
            // label默认蓝框白底左上角显示，样式className为：amap-marker-label
            marker.setLabel({
              offset: new AMap.Pixel(20, 20),  //设置文本标注偏移量
              content: provinces[i].elevators,
              direction: 'right' //设置文本标注方位
            });

       //     } 

        }

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
              this.mapConfig.center = [this.lng, this.lat]
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
          this.map.addControl(new AMap.ToolBar({
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
