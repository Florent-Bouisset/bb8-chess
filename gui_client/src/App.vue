<script setup lang="ts">
import ChessGame from "./components/ChessGame.vue";
const restartGame = () => {
  console.log("Restart clicked");
};

const changeDifficulty = () => {
  console.log("Difficulty clicked");
};
</script>

<template>
  <div class="wrapper">
    <div class="menu">
      <button @click="restartGame">♻️ Restart</button>
      <button @click="changeDifficulty">⚙️ Difficulty</button>
    </div>
    <div class="board-container">
      <ChessGame />
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
}

.board-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  padding: 10px; /* optional, to add breathing room */
}

.menu {
  display: flex;
  justify-content: center;
  gap: 10px;
  padding: 10px;
  border-bottom: 1px solid #333;
  background-color: #1e1e1e;
  margin-bottom: 20px;
}

.menu button {
  padding: 10px 15px;
  font-size: 14px;
  cursor: pointer;
  border: 1px solid #444;
  background-color: #333;
  color: #fff;
  border-radius: 5px;
  transition: background 0.2s;
}

.menu button:hover {
  background-color: #444;
}
</style>
