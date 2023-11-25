<template>
  <body class="">
    <Header></Header>
    <div
      class="bg-gradient-to-r from-blue-800 to-blue-600 2xl:px-48 xl:px-44 lg:px-32 md:px-24 sm:px-16 px-6"
    >
      <div class="z-20">
        <Database :db_list=" database" />
      </div>
      <div class="z-20">
        <WarningTable :act_list="warnings" />
      </div>
      <div class="flex justify-left gap-4 pt-8">
        <div class="bg-whitesmoke w-1/3 rounded-lg"><BarChart :label_name="`Распределение групп тем`" :dataset="warnings.group_stats" /></div>
        <div class="bg-whitesmoke w-1/3 rounded-lg"><BarChart :label_name="`Распределение тем`" :dataset="warnings.theme_stats"/></div>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>
<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Database from "@/components/Database.vue";
import FormsFile from "@/components/FormsFile.vue";
import WarningTable from "@/components/WarningTable.vue";
import axios from "axios";
import RewiewForm from "@/components/RewiewForm.vue";
import BarChart from "@/components/charts/BarChart.vue";
import RadarChart from "@/components/charts/RadarChart.vue";
export default {
  components: {
    Header,
    Footer,
    FormsFile,
    RewiewForm,
    Database,
    WarningTable,
    BarChart,
    RadarChart,
  },
  data() {
    return {
      database: [],
      warnings: []
    };
  },
  methods:{
    get_database() {
      this.isError = false;
      this.isLoading = true;
      axios
        .get(
          `https://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/total_db`
          
        )
        .then(
          (response) => (
            (this.database = response.data),
            console.log(this.responed_data),
            (this.isLoading = false)
          )
        )
        .catch((response) => ((this.isLoading = false), (this.isError = true)));
    },
    get_actual() {
        this.isError = false;
        this.isLoading = true;
        axios
          .get(
            `https://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/extra_issues`
            
          )
          .then(
            (response) => (
              (this.warnings = response.data),
              console.log(response.data),
              (this.isLoading = false)
            )
          )
          .catch((response) => ((this.isLoading = false), (this.isError = true)));
      },
  },
  created() {
    this.get_actual()
    this.get_database()
    setTimeout(console.log("Ready!"), 1500)
    
  }
};
</script>
