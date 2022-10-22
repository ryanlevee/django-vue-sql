<template>
    <div class="py-4 fs-3 fw-normal">
      {{word}} ({{wordsLeft}} left)
    </div>
</template>

<script>
  export default {
    name: 'Word-El',
    props: {
      word: String,
      wordsLeft: Number,
    }
  }
</script>

<style> /* scoped isn't working */
  #word {
    font-size: 1.4em;
    margin: auto;
    width: 90%;
  }
</style>