<template>
  <body class="">
    <Header></Header>
    <div
      class="bg-gradient-to-r from-blue-800 to-blue-600 2xl:px-48 xl:px-44 lg:px-32 md:px-24 sm:px-16 px-6"
    >
      <div class="z-20">
        <Database :org_list="this.org_list" />
      </div>
      <div class="z-20">
        <WarningTable :org_list="this.org_list" />
      </div>
      <div class="flex justify-left gap-4 pt-8">
        <div class="bg-whitesmoke w-1/3 rounded-lg"><BarChart /></div>
        <div class="bg-whitesmoke w-1/3 rounded-lg"><BarChart /></div>
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
      org_list: [],
    };
  },
  mounted() {
    axios
      .get(
        `http://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/total_organisations`
      )
      .then(
        (response) => (
          (this.org_list = response.data.organisations),
          console.log(this.org_list)
        )
      );
  },
};
</script>
