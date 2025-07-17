<script setup lang="ts">
import ChessGame from "./components/ChessGame.vue";
</script>

<template>
  <main>
    <ChessGame />
  </main>
</template>

<!-- <style>
main {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f4f4;
}
</style> -->

<style>
body {
  display: flex;
  flex-wrap: wrap;
}

body > div {
  margin: 10px;
}

.chessground {
  width: 500px;
  height: 500px;
}

cg-board {
  background-color: #bfcfdd;
}
</style>
