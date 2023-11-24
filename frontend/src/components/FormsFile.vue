<template>
  <div>
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
          .csv
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
  <div class="rounded-lg pt-4">
    <p class="text-left pb-2 font-bold text-xl text-whitesmoke">Результат</p>
    <div
      class="sm:rounded-lg rounded-lg overflow-auto h-[500px] xl:max-w-[1800px] lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
    >
      <table
        class="w-full text-sm text-gray-500 table-auto 2xl:table-fixed text-center"
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
              class="px-6 py-3 2xl:w-32 cursor-pointer hover:text-blue-600"
            >
              Дата
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-48 cursor-pointer hover:text-blue-600"
            >
              Группа тем
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-blue-600"
            >
              Тема
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-64 cursor-pointer hover:text-blue-600"
            >
              Локация
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-72 cursor-pointer hover:text-blue-600"
            >
              Текст инцедента
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-60 cursor-pointer hover:text-blue-600"
            >
              Исполнитель
            </th>
          </tr>
        </thead>
        <tbody class="font-semibold">
          <tr
            v-for="i in 10"
            class="bg-white border-b hover:bg-gray-50 cursor-pointer hover:text-blue-600"
          >
            <th
              scope="row"
              class="px-2 py-2 max-w-lg font-medium text-gray-900 whitespace-nowrap truncate"
            >
              1
            </th>
            <td class="px-6 py-4">2023-11-24</td>
            <td class="px-6 py-4 text-center">group</td>
            <td class="px-6 py-4 text-justify">
              Нарушение правил очистки дорог от снега и наледи/Обращения о
              необходимости очистить тратуар от снега и наледи
            </td>
            <td class="px-6 py-4">
              Россия, г.Санкт-Петербург, ул.Красного петуха, д.6, к.3, кв.124
            </td>
            <td class="px-6 py-4 text-center">На улице не убран снег</td>
            <td class="px-6 py-4 hover:text-blue-600 cursor-pointer">
              <select
                id="companyFile"
                class="bg-gray-50 border border-gray-300 cursor-pointer text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
              >
                <option selected>Выберите исполнителя</option>
                <div>Поиск</div>
                <option v-for="(org, index) in org_list" :key="index" :value="index">{{org}}</option>
              </select>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";


export default {

  props: {
    org_list: Array
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
      axios
        .post(`https://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/add_file_all_pavlov`, formData, {
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
