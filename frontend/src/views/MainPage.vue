<template>
  <body class="">
    <Header></Header>
    <div class="bg-gradient-to-r from-blue-800 to-blue-600 2xl:px-56 xl:px-44 lg:px-32 md:px-24 sm:px-16 px-48">
      <div class="z-20">
        <RewiewForm />
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
          <FormsFile></FormsFile>
        </div>
      </div>
      <div class="sm:px-24 px-8 py-12">
        <QuestionBlog :question_list="question_list"></QuestionBlog>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import FormsFile from "@/components/FormsFile.vue";
import QuestionBlog from "@/components/QuestionBlog.vue";
import axios from "axios";
import RewiewForm from "@/components/RewiewForm.vue";
export default {
  components: { Header, Footer, FormsFile, QuestionBlog, RewiewForm },
  data() {
    return {
      question_list: [],
    };
  },
  mounted() {
    axios
      .get(`http://${process.env.VUE_APP_USER_IP_WITH_PORT}/tableslist/`)
      .then(
        (response) => (
          (this.question_list = response.data.result),
          console.log(response.data.result)
        )
      );
  },
};
</script>

<style></style>
