<template>
    <div class="border-idealBlue border-[6px] rounded-lg shadow-cards">
      <yandex-map @map-was-initialized="handler" @click="changeMyPos" :coords="coords" :use-object-manager="true"
        :object-manager-clusterize="true"   :settings="settings" :zoom="3" :cluster-options="clusterOptions">
        <ymap-marker   v-for="(item, index) in loc_list" :key="index" :coords="[item[0], item[1]]"
          :markerId="item.id" :cluster-name="1"   />
            
      </yandex-map>
      
    </div>
  </template>
  
  <script>
  import { yandexMap, ymapMarker, loadYmap } from "vue-yandex-maps";
  import { mapActions, mapGetters } from 'vuex';
  
  
  const settings = {
    apiKey: "9b855f9b-6853-4cb2-b2f8-f02951d693c4",
    lang: "ru_RU",
    coordorder: "latlong",
    enterprise: false,
    version: "2.1",
  };
  
  export default {
    components: { yandexMap, ymapMarker },
    data() {
      return {
        map: null,
        ymaps_user: null,
        coords: [55.753215, 36.622504],
        settings: settings,
      };
    },
    methods: {
  },
  props: {
    theme: String,
    text: String,
    loc_list: Array,
    },
  }
  </script>
  
  <style>
  .red {
    color: red;
  }
  
  .ymap-container {
    width: 100%;
    height: 24vh;
  }
  
  .ballon_header {
    font-size: 16px;
    margin-top: 0;
    margin-bottom: 10px;
    color: #708090;
  }
  
  .ballon_body {
    font-size: 14px;
    text-align: center;
  }
  
  .ballon_footer {
    font-size: 12px;
    text-align: right;
    border-top: 1px solid #7d7d7d;
    color: #7d7d7d;
    margin-top: 10px;
  }
  
  .description {
    display: block;
    color: #999;
    font-size: 10px;
    line-height: 17px;
  }
  </style>