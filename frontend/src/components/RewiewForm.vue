<template>
  <div>
    <div
      class="text-whitesmoke font-black z-[10] font-roboto 2xl:text-7xl xl:text-7xl lg:text-7xl md:text-7xl w-20 pt-12 sm:text-7xl text-5xl"
    >
      Введите отзыв
    </div>
    <div>
      <form class="w-full">
        <div class="pt-4">
          <input
            v-model="input_text"
            autofocus
            type="text"
            id="large-input"
            class="block w-full p-4 text-gray-900 font-roboto font-medium rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex justify-end pt-2">
          <button
            type="submit"
            @click="submit_text()"
            class="text-white border-[1px] 2xl:text-lg hover:bg-blue-900 hover:border-blue-900 hover:border-[1px] duration-150 focus:ring-4 focus:outline-none focus:ring-blue-700 font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
          >
            Отправить отзыв
          </button>
        </div>
      </form>
    </div>
    <div v-if="isLoading" role="status" class="flex justify-center pt-20">
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
    <div v-else class="rounded-lg pt-1">
      <p class="text-left pb-2 font-bold text-xl text-whitesmoke">Результат</p>
      <div
        class="sm:rounded-lg rounded-lg overflow-auto h-full xl:max-w-[1800px] lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
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
            <tr class="bg-white border-b hover:bg-gray-50 cursor-pointer">
              <td class="px-6 py-4 hover:text-blue-600 text-center">
                {{ responed_data.date }}
              </td>
              <td class="px-6 py-4 text-center hover:text-blue-600">
                {{ responed_data.group }}
              </td>
              <td class="px-6 py-4 text-center hover:text-blue-600">
                {{ responed_data.theme }}
              </td>
              <td class="px-6 py-4 hover:text-blue-600 text-center">
                {{ responed_data.ner }}
              </td>
              <td class="px-6 py-4 text-justify hover:text-blue-600">
                {{ responed_data.message }}
              </td>
              <td class="px-6 py-4 hover:text-blue-600 cursor-pointer">
                <select
                  id="company"
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
      input_text: "",
      responed_data: [],
      isLoading: false,
      isError: false,
    };
  },
  methods: {
    submit_text() {
      this.isError = false;
      this.isLoading = true;
      axios
        .post(
          `https://${process.env.VUE_APP_USER_IP_WITH_PORT}/api/add_message_all_pavlov`,
          { message: this.input_text }
        )
        .then(
          (response) => (
            (this.responed_data = response.data),
            console.log(this.responed_data),
            (this.isLoading = false)
          )
        )
        .catch((response) => ((this.isLoading = false), (this.isError = true)));
    },
  },
};
</script>
