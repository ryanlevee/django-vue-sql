<template>
  <div class="pt-4 fs-5 fw-semibold" style="font-variant:small-caps">
  <div class="row my-3 mx-auto ms-1">
    <label :for="id" class="col my-1">{{label}}</label>
    <select class="col form-select ms-3 me-3" :id="id" :value="currentValue"
      @input="$emit('update:currentValue', $event.target.value)">
      <option v-for="option in options" :key="option[1]"
        :value="option[1]">{{option[0]}}</option>
    </select>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'SelectInput',
    props: {
      id: String,
      label: String,
      options: Array,
      currentValue: String
    },
  }
</script>