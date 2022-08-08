<template>
  <div v-if="pageIs('home')">
    <HomePage></HomePage>
  </div>
  <div v-if="pageIs('chat')">
    <ChatPage></ChatPage>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { HomePage, ChatPage } from './Pages/index'
export default defineComponent({
  // components: { HomePage, ChatPage },
  components: { ChatPage },
  data() {
    return {
      page: 'chat',
    }
  },
  methods: {
    pageIs(key) {
      return this.page === key
    },
  },
  mounted() {
    console.log('Mounted!!')
  },
})
</script>
