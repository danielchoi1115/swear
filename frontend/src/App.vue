<template>
  <html>
    <head>
      <title>Chat</title>
    </head>
    <body>
      <button @click="connect">Connect</button>
      <button @click="disconnect">Disconnect</button>
      <div>{{ connected }}</div>
      <h1>WebSocket Chat</h1>
      <input type="text" id="messageText" autocomplete="off" />
      <button @click="sendMessage">Send</button>
      <ul id="messages"></ul>
    </body>
  </html>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
declare let websocket: WebSocket

export default defineComponent({
  data() {
    return {
      isDark: true,
      ws: websocket as WebSocket,
      connected: 'null',
    }
  },
  // beforeMount() {

  // },
  methods: {
    sendMessage(event: Event) {
      var input = document.getElementById('messageText') as HTMLInputElement
      this.ws.send(input.value)
      input.value = ''
      event.preventDefault()
    },
    setConnection(status: string) {
      this.connected = status
    },
    connect() {
      websocket = new WebSocket('ws://localhost:8000/ws/1')
      this.ws.onmessage = function (event) {
        var messages = document.getElementById('messages')
        var message = document.createElement('li')
        var content = document.createTextNode(event.data)
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
    },
    disconnect() {
      this.ws.close()
    },
  },
})
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
