<template>
  <el-scrollbar>
    <ChatListItem v-for="item in 10" :key="item"></ChatListItem>
  </el-scrollbar>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ChatListItem from './ChatListItem.vue'
export default defineComponent({
  components: { ChatListItem },
})
</script>
