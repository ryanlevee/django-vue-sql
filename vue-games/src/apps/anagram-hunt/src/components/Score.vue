<template>
  <strong class="ms-2">Score: {{score}}</strong>
</template>

<script>
  export default {
    name: 'Score-El',
    props: {
      score: Number,
    }
  }
</script>