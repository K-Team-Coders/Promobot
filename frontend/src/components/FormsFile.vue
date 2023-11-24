<template>
  <div>
    <div
      class="bg-gray-50 w-full px-4 py-4 border-[1.5px] shadow-md rounded-lg"
    >
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
    <div v-if="isLoading" role="status" class="flex justify-center py-20">
      <svg
        aria-hidden="true"
        class="inline w-20 h-20 text-gray-200 animate-spin fill-blue-600"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
      <span class="sr-only">Загрузка...</span>
    </div>
    <div
      v-else-if="isError"
      class="text-whitesmoke font-black z-[10] font-roboto 2xl:text-xl xl:text-xl lg:text-xl md:text-xl w-96 pt-12 sm:text-xl text-xl"
    >
      Ошибка. Попробуйте еще раз
    </div>
    <div v-else class="rounded-lg pt-4">
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
                class="px-6 py-3 2xl:w-32 cursor-pointer hover:text-blue-600"
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
                class="px-6 py-3 2xl:w-40 cursor-pointer hover:text-blue-600"
              >
                Тема
              </th>
              <th
                scope="col"
                class="px-6 py-3 2xl:w-44 cursor-pointer hover:text-blue-600"
              >
                Локация
              </th>
              <th
                scope="col"
                class="px-6 py-3 2xl:w-96 cursor-pointer hover:text-blue-600"
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
              v-for="(el, index) in response_data" :key="index"
              class="bg-white border-b hover:bg-gray-50 cursor-pointer hover:text-blue-600"
            >
              <th
                scope="row"
                class="px-2 py-2 max-w-lg font-medium text-gray-900 whitespace-nowrap truncate"
              >
                {{index + 1}}
              </th>
              <td class="px-6 py-4">{{el.date}}</td>
              <td class="px-6 py-4 text-center">{{ el.group }}</td>
              <td class="px-6 py-4 text-justify">
                {{el.theme}}
              </td>
              <td class="px-6 py-4">
                <ul> 
                  <li v-for="loc in el.loc" :key="loc">{{ loc }} </li>
                </ul>
              </td>
              <td class="px-6 py-4 text-center">{{ el.text }}</td>
              <td class="px-6 py-4 hover:text-blue-600 cursor-pointer">
                <select
                  id="companyFile"
                  class="bg-gray-50 border border-gray-300 cursor-pointer text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                >
                  <option selected>Выберите исполнителя</option>
                  <div>Поиск</div>
                  <option
                    v-for="(org, index) in org_list"
                    :key="index"
                    :value="index"
                  >
                    {{ org }}
                  </option>
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
    org_list: Array,
  },
  data() {
    return {
      isError: false,
      files: "",
      text: "",
      isLoading: false,
      response_data: [],
    };
  },
  methods: {
    submitFiles() {
      this.isLoading = true;
      this.isError = false;
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("file", file);
      }
      axios
        .post(
          `https://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/add_file_all_pavlov`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then(
          (response) => (
            console.log("SUCCESS!"),
            console.log(response.data.result),
            this.response_data = response.data.result,
            this.isLoading = false
          )
        )
        .catch((response) => ((this.isLoading = false), (this.isError = true)));
    },
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
