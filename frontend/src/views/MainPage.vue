<template>
  <body class="">
    <Header></Header>
    <div class="bg-gradient-to-r from-blue-800 to-blue-600 2xl:px-48 xl:px-44 lg:px-32 md:px-24 sm:px-16 px-6">
      <div class="z-20">
        <RewiewForm :org_list="this.org_list"/>
      </div>
      <div class="pt-24">
        <div class="w-full bg-gray-200 rounded-full h-1">
          <div class="bg-blue-600 h-1 rounded-full" style="width: 0%"></div>
        </div>
      </div>
      <div class="pt-4">
        <div
          class="text-whitesmoke font-black z-[10] font-roboto 2xl:text-7xl xl:text-7xl lg:text-7xl md:text-7xl sm:text-7xl text-5xl w-1/2 pt-12"
        >
          Выберите файл для анализа
        </div>
        <div class="pt-4">
          <FormsFile :org_list="org_list"></FormsFile>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Database from "@/components/Database.vue"
import FormsFile from "@/components/FormsFile.vue";
import WarningTable from "@/components/WarningTable.vue";
import axios from "axios";
import RewiewForm from "@/components/RewiewForm.vue";
export default {
  components: { Header, Footer, FormsFile, RewiewForm, Database, WarningTable },
  data() {
    return {
      org_list: []
    };
  },
  mounted() {
    axios
      .get(`http://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/total_organisations`)
      .then(
        (response) => (
          (this.org_list = response.data.organisations),
          console.log(this.org_list)
        )
      );
  },
};
</script>

<style></style>
