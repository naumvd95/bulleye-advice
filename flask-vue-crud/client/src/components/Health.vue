<template>
  <div class="container">

    <b-button variant="danger" disabled>
      <b-spinner small></b-spinner>
      <span class="sr-only">Loading...</span>
    </b-button>

    <b-button variant="light" disabled>
      {{ msg }}
    </b-button>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Healthcheck',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      // TODO define backend variable
      const path = 'http://localhost:5000/healthcheck';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

