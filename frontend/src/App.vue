<template>
  <html class="bg-cool-gray-100">
    <head>
      <title>Chat</title>
    </head>
    <body class="">
      <button @click="connect" class="bg-blue-500 hover:bg-blue-700">Connect</button>
      <button @click="disconnect" class="bg-blue-500 hover:bg-blue-700">Disconnect</button>
      <div>{{ connected }}</div>
      <h1>WebSocket Chat</h1>
      <input type="text" class="border-red-500 border-solid border-4" id="messageText" autocomplete="off" />
      <button @click="sendMessage" class="bg-red-400">Send</button>
      <ul id="messages"></ul>

      <!-- <SwContainer> </SwContainer> -->
    </body>
  </html>
</template>

<script lang="ts">
import { SwContainer } from './layouts/index'
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      isDark: true,
      connected: 'null',
      ws: {} as WebSocket,
    }
  },
  methods: {
    sendMessage(event: Event) {
      // if(this.ws === null || this.ws.readyState)
      var input = document.getElementById('messageText') as HTMLInputElement
      this.ws.send(input.value)
      input.value = ''
      event.preventDefault()
    },
    setConnection(status: string) {
      this.connected = status
    },
    async connect() {
      if (isEmpty(this.ws) || this.ws.readyState !== 1) {
        this.ws = await new WebSocket('ws://localhost:8000/ws/1')
        this.ws.onmessage = function (event: Event) {
          var messages = document.getElementById('messages')
          var message = document.createElement('li')
          var content = document.createTextNode((event as MessageEvent).data)
          message.appendChild(content)
          if (messages) {
            messages.appendChild(message)
          }
        }
        this.ws.onopen = function () {
          console.log('connection open!!')
        }
        this.ws.onclose = function () {
          console.log('connection closed!!')
        }
      } else {
        console.log('connection already made')
        return
      }
    },
    disconnect() {
      if (isEmpty(this.ws) || this.ws.readyState !== 1) {
        console.log('connection already closed')
        return
      } else {
        this.ws.close()
      }
    },
  },
})

function isEmpty(object: any) {
  for (const property in object) {
    return false
  }
  return true
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
