<template>
  <div class="container-fluid">
  <div class="row justify-content-center">
  <div class="col">

    <button class="form-control btn mb-5 mt-3 py-2 text-white
    fs-5 fw-semibold border-dark border-top-0 border-start-0"
    style="background-color:#848F9B;text-shadow:1px 1px black"
      @click="$emit('play-button-click')">Play!</button>
  </div>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'PlayButton'
  }
</script>