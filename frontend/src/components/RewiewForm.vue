<template>
  <div
    class="text-whitesmoke font-black z-[10] font-roboto text-9xl w-20 pt-12"
  >
    Введите отзыв
  </div>
  <div>
    <form class="w-full">
      <div class="pt-4">
        <input
          type="text"
          id="large-input"
          class="block w-full p-4 text-gray-900 font-roboto font-medium rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
      <div class="flex justify-end pt-2">
        <button
          type="submit"
          class="text-white border-[1px] 2xl:text-lg hover:bg-blue-900 hover:border-blue-900 hover:border-[1px] duration-150 focus:ring-4 focus:outline-none focus:ring-blue-700 font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
        >
          Отправить отзыв
        </button>
      </div>
    </form>
  </div>

  <div class="rounded-lg pt-1">
    <p class="text-left pb-2 font-bold text-xl text-whitesmoke">
      Результат
    </p>
    <div
      class="sm:rounded-lg rounded-lg overflow-auto h-full xl:max-w-[1800px] lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
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
          <tr
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
