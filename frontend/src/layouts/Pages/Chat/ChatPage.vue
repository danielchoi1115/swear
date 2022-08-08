<template>
  <div class="grid grid-rows-1 grid-cols-3 gap-4 max-w-screen-2xl">
    <div class="col-start-1 col-end-4 row-start-1 row-end-1 border-2">Header2</div>
  </div>
  <div class="grid grid-rows-1 grid-cols-3 gap-4max-w-screen-2xl h-96">
    <div class="col-start-1 col-end-1 row-start-1 border-2">
      <ChatList></ChatList>
    </div>
    <div class="col-start-2 col-end-4 row-start-1 border-2">
      <ChatBox></ChatBox>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import ChatBox from './ChatBox.vue'
import ChatList from './ChatList.vue'
export default defineComponent({
  components: { ChatBox, ChatList },
})
</script>
