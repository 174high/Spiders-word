<template>
  <div id="app">
    <div class="g-wraper" v-hljs>
      <div class="m-part">
        <!--<h3 class="title">Watch List </h3> -->
        <ul  class="watchlist">Watch List </ul >
        <ul class="list">        
        <select name="public-choice" v-model="couponSelected" @change="getCouponSelected">                                        
        <option :value="coupon.id" v-for="coupon in couponList" :key="coupon.id" >{{coupon.name}}</option>                                    
        </select>
<!--
          <option value="All units">All units</option>
          <option value="BIC5 (EU) release 2">BIC5 (EU) release 2</option>
          <option value="BIC5 (EU) release 4 and higher">BIC5 (EU) release 4 and higher</option>
          <option value="BIC7 (EU) release 1 and higher">BIC7 (EU) release 1 and higher</option>
          <option value="IoEE Cube Test Equipments">IoEE Cube Test Equipments</option>
          <option value="MX7 (EU)">MX7 (EU)</option>
          <option value="MX7 (EU) release 2">MX7 (EU) release 2</option>
          <option value="S2X00/5400/Eurolift">S2X00/5400/Eurolift</option>
          <option value="S3X00/5300">S3X00/5300</option>
          <option value="S5500">S5500</option>
          <option value="S6200">S6200</option>
          <option value="S6300">S6300</option>
          <option value="Schindler Direct Units">Schindler Direct Units</option>
          <option value="Service Contract Active">Service Contract Active</option>
          <option value="SMART">SMART</option>
 </select>-->

        </ul>
        <!-- <h4 class="title">Select Portfolio</h4> -->
        <mapDrag @drag="dragMap" class="mapbox"></mapDrag>
        <ul class="info">
          <li><span>经度：</span>{{ dragData.lng }}</li>
          <li><span>纬度：</span>{{ dragData.lat }}</li>
          <li><span>地址：</span>{{ dragData.address }}</li>
          <li><span>最近的路口：</span>{{ dragData.nearestJunction }}</li>
          <li><span>最近的路：</span>{{ dragData.nearestRoad }}</li>
          <li><span>最近的POI：</span>{{ dragData.nearestPOI }}</li>
        </ul>
      </div>   
    </div>
  </div>
</template>

<script>
import mapDrag from './components/mapDrag'
export default {
  name: 'app',
  components: {
    mapDrag
  },
  data () {
    return {
      dragData: {
        lng: null,
        lat: null,
        address: null,
        nearestJunction: null,
        nearestRoad: null,
        nearestPOI: null,        
      },
      couponList:[
             {
                 id: 'All units',
                  name: 'All units'
              },
              {
                   id: 'BIC5 (EU) release 2',
                   name: 'BIC5 (EU) release 2'
               },
               {
                   id: 'IC5 (EU) release 4 and higher',
                   name: 'IC5 (EU) release 4 and higher'
               },
               {
                   id: 'BIC7 (EU) release 1 and higher',
                    name: 'BIC7 (EU) release 1 and higher'
              },
              {
                   id: 'IoEE Cube Test Equipments',
                  name: 'IoEE Cube Test Equipments'
              },
              {
                 id: 'MX7 (EU)',
                  name: 'MX7 (EU)'
              },
              {
                 id: 'MX7 (EU) release 2',
                  name: 'MX7 (EU) release 2'
              },
            {
                 id: 'S2X00/5400/Eurolift',
                 name: 'S2X00/5400/Eurolift'
              },
            {
                 id: 'S3X00/5300',
                  name: 'S3X00/5300'
              },
            {
                 id: 'S5500',
                  name: 'S5500'
              },
              {
                 id: 'S6200',
                 name: 'S6200'
              },
              {
                 id: 'S6300',
                  name: 'S6300'
              },
              {
                  id: 'Schindler Direct Units',
                  name: 'Schindler Direct Units'
              },
              {
                 id: 'Service Contract Active',
                  name: 'Service Contract Active'
              },
              {
                 id: 'SMART',
                  name: 'SMART'
              }, 
        ],                 
      couponSelected: '',  
    }
  },

  created(){
//如果没有这句代码，select中初始化会是空白的，默认选中就无法实现
    this.couponSelected = this.couponList[0].id;
  },

  methods: {
    dragMap (data) {
      this.dragData = {
        lng: data.position.lng,
        lat: data.position.lat,
        address: data.address,
        nearestJunction: data.nearestJunction,
        nearestRoad: data.nearestRoad,
        nearestPOI: data.nearestPOI
      }
    },

    getCouponSelected(){
        //获取选中的优惠券
        //console.log(this.dragData.couponSelected)
    }
  }

}
</script>

<style>
body{ margin: 0; }
.page-header{
  color: #fff; text-align: center; background: #159957;
  background-image: -webkit-linear-gradient(330deg,#155799,#159957);
  background-image: linear-gradient(120deg,#155799,#159957);
  padding: 3rem 4rem; margin-bottom: 30px;
}
.page-header h1{ margin: 0; font-size: 40px; }
.page-header p{ color: #ccc; margin: 0; margin-bottom: 30px; }
.page-header a{ display: inline-block; border: 1px solid #fff; margin-right: 10px; line-height: 40px; padding: 0 20px; border-radius: 4px; color: #fff; text-decoration: none; transition: all .3s; }
.page-header a:hover{ background: #fff; color: #333; }
.g-wraper{ width: 1000px; margin: 0 auto; color: #666; font-size: 16px; line-height: 30px; }
.m-part{ margin-bottom: 30px; }
.m-part::after{ content: ''; display: block; clear: both; }
.m-part .title{ font-size: 30px; line-height: 60px; margin-bottom: 10px; color: #333; }
.m-part .mapbox{ width: 600px; height: 400px; margin-bottom: 20px; float: left; }
.m-part .info{ margin: 0; padding: 0; list-style: none; line-height: 30px; margin-left: 620px; }
.m-part .watchlist{ margin: 0; padding: 0; list-style: none; line-height: 30px; margin-left: 10px; float: left;}
.m-part .list{ margin: 0; padding: 0; list-style: none; line-height: 30px; margin-left: 95px; }
.m-part .info span{ display: block; color: #999; }
.m-part ol{ line-height: 40px; margin-left: 0; padding-left: 0; }
.m-part pre{ padding: 10px 20px; line-height: 30px; border-radius: 3px; box-shadow: 0 0 15px rgba(0,0,0,.5); }
.m-footer{ background: #eee; line-height: 60px; text-align: center; color: #999; font-size: 12px; }
.m-footer a{ margin:  0 5px; color: #999; text-decoration: none; }
</style>
