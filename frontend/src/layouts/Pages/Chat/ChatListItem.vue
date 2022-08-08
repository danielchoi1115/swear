<template>
  <div id="item-container" class="bg-red-300 border-2">
    <div id="avatar" class="">
      <el-avatar class="" :size="50" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
    </div>
    <div id="middle" class="px-8">
      <div class="">name</div>
      <div class="">recent chat</div>
    </div>
    <div id="time" class="justify-end">9:00AM</div>
  </div>
  <!-- <el-divider /> -->
</template>

<style scoped>
#item-container {
  display: flex;
  justify-content: space-between;
}
#middle {
  display: flex;
  justify-content: start;
}
</style>
