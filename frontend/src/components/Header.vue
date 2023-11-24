<template>
  <header class="bg-gradient-to-r from-blue-800 to-blue-600 border-b-[1px]">
    <div class="flex justify-between items-center py-2.5 2xl:px-[196px]">
      <div class="flex text-center items-center justify-center mt-1.5">
        <router-link
          to="/"
          class="xl:text-2xl text-lg font-roboto font-medium hover:text-gray-300 text-whitesmoke"
          >Система обработки обращений граждан SCORIC</router-link
        >
      </div>
      <router-link
        to="/database"
        class="xl:text-2xl text-lg font-roboto font-medium hover:text-gray-300 text-whitesmoke cursor-pointer"
        >База данных</router-link
      >
    </div>
  </header>
</template>

<script>
export default {};
</script>
