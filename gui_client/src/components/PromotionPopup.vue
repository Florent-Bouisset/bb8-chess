<!-- components/PromotionPopup.vue -->
<template>
  <div v-if="visible" class="promotion-popup cg-wrap">
    <div
      :key="type"
      v-for="type in types"
      class="promotion-item"
      @click="choose(type)"
    >
      <piece class="white" :class="type" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineEmits } from "vue";

const emit = defineEmits<{
  (e: "selected", piece: string): void;
}>();

const visible = ref(true);
const types = ["queen", "rook", "bishop", "knight"];

function choose(type: string) {
  visible.value = false;
  const map: Record<string, string> = {
    queen: "q",
    rook: "r",
    bishop: "b",
    knight: "n",
  };
  emit("selected", map[type]);
}
</script>

<style scoped>
.promotion-popup {
  position: absolute;
  display: flex;
  background: #bfcfdd;
  border: 1px solid black;
  z-index: 10;
  display: flex;
  top: 100px;
  left: 25vmin;
  width: 40vmin;
  height: 10vmin;
}

.promotion-item {
  position: relative;
  display: flex;
  background: #bfcfdd;
  border: 1px solid black;
  z-index: 10;
  display: flex;
  width: 25%;
  height: auto;
  box-sizing: border-box;
}

.promotion-piece {
  padding: 5px;
  cursor: pointer;
}
piece {
  width: 100%;
  height: auto;
  position: static;
  cursor: pointer;
}
</style>
