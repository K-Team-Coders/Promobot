<template>
  <div class="bg-gray-50 w-full px-4 py-4 border-[1.5px] shadow-md rounded-lg">
    <form action="">
      <div class="flex justify-start">
        <input
          v-on:change="handleFilesUpload()"
          class="w-full text-sm text-gray-700 border-[0.5px] py-1 px-2 border-blue-500 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
          aria-describedby="file_input_help"
          id="files"
          ref="files"
          type="file"
        />
        <p class="mt-2.5 ml-2 text-sm text-gray-500" id="file_input_help">
          .json
        </p>
      </div>
      <div class="flex justify-end pt-2">
        <button
          @click="submitFiles()"
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 duration-150 focus:outline-none focus:ring-blue-700 font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
        >
          Отправить файл
        </button>
      </div>
    </form>
  </div>
  <div class="rounded-lg pt-8">
    <p class="text-left pb-2 font-bold text-xl text-whitesmoke">Результат</p>
    <div
      class="sm:rounded-lg rounded-lg overflow-auto h-[400px] xl:max-w-[1800px] lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
    >
      <table
        class="w-full text-xs text-gray-500 table-auto 2xl:table-fixed text-center"
      >
        <thead class="text-xs text-gray-700 bg-gray-50 font-bold">
          <tr class="">
            <th
              scope="col"
              class="px-1 py-3 2xl:w-10 cursor-pointer hover:text-blue-600"
            >
              ID
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-96 cursor-pointer hover:text-blue-600"
            >
              Группа тем
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-blue-600"
            >
              Текст инцедента
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-[500px] cursor-pointer hover:text-blue-600"
            >
              Тема
            </th>
          </tr>
        </thead>
        <tbody class="font-semibold">
          <tr v-for=" i in 10"
            class="bg-white border-b hover:bg-gray-50 cursor-pointer hover:text-blue-600"
          >
            <th
              scope="row"
              class="px-2 py-2 max-w-lg font-medium text-gray-900 whitespace-nowrap truncate"
            >
              1
            </th>
            <td class="px-6 py-4">Животные, асфальт, город</td>
            <td class="px-6 py-4 text-justify">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis
              autem possimus quae, atque nostrum nesciunt eos assumenda corrupti
              veritatis aliquid voluptate perferendis? Debitis accusantium saepe
              excepturi. Ea cupiditate a provident.
            </td>
            <td class="px-6 py-4">
              Еженедельное закапывание в асфальт пьяных кого-то
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import LoadingPage from "./LoadingPage.vue";

export default {
  components: {
    LoadingPage,
  },
  data() {
    return {
      is_Error: false,
      IP: process.env.VUE_APP_USER_IP_WITH_PORT,
      files: "",
      text: "",
      isTyping: false,
      is_Loading: false,
      colors: ["#4487BE", "#FF7E00", "#222"],
    };
  },
  methods: {
    submitFiles() {
      console.log(this.files);
      this.is_Loading = true;
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("file", file);
      }
      console.log(this.IP);
      axios
        .post(`http://${this.IP}/files/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(function () {
          console.log("SUCCESS!!");
          location.reload();
        })
        .catch(function (response) {
          console.log("FAILURE!!");
          if (response.statusCode == 400) {
            alert("Такой файл уже был загружен! Загрузите другой.");
          }
        })
        .finally(function () {
          is_Loading = false;
        });
    },
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
