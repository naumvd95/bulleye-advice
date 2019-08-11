<template>
  <div class="container">
    <div class="row">
      <div class="col-md-auto">
        <b-card bg-variant="light" text-variant="red" title="Bulls-eye advice">
          <b-card-text>
            Perhaps your advice will save someone's life.
            Or help them to find a cafe with a best pho-bo. Who knows.
          </b-card-text>
          <b-button href="#" variant="danger" v-b-modal.advice-modal>Advise them</b-button>
        </b-card>
        <alert :message="message" v-if="showMessage"></alert>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Advice</th>
              <th scope="col">Author</th>
              <th scope="col">Have you tried?</th>
              <th scope="col">Tags</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(advice, index) in advices" :key="index">
              <td>{{ advice.title }}</td>
              <td>{{ advice.author }}</td>
              <td>
                <span v-if="advice.verified">Yes</span>
                <span v-else>No</span>
              </td>
              <td>{{ advice.tags }}</td>
              <td>
                <b-button-group size="sm">
                  <b-button variant="danger">Bulls-eye!</b-button>
                  <b-button variant="dark">Update</b-button>
                  <b-button>Delete</b-button>
                </b-button-group>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addAdviceModal"
             id="advice-modal"
             title="Add new advice"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">

        <b-form-group id="form-title-group"
                      label="Title:"
                      label-align="left"
                      description=""
                      :invalid-feedback="invalidFeedback"
                      :state="state"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addAdviceForm.title"
                        required
                        :state="state"
                        trim
                        placeholder="Boobs better than beer">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-author-group"
                      label="Author:"
                      label-align="left"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addAdviceForm.author"
                        placeholder="Anonymous">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-verified-group">
          <b-form-checkbox-group v-model="addAdviceForm.verified" id="form-checks">
            <b-form-checkbox value="true">Have you tried?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-form-group id="form-tags-group"
                      label="Tags:"
                      label-align="left"
                      label-for="form-tags-input">
          <b-form-input id="form-tags-input"
                        type="text"
                        v-model="addAdviceForm.tags"
                        placeholder="TODO add tag-push loop">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="danger">Submit</b-button>
        <b-button type="reset" variant="dark">Reset</b-button>

      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  computed: {
    // Below 2 methods for defining 100-symbol restriction for advice and monitor it.
    state() {
      const al = this.addAdviceForm.title.length;
      return (al > 0 && al < 100);
    },
    invalidFeedback() {
      if (this.addAdviceForm.title.length > 100) {
        return 'Blah Blah Blah, write briefly and to the point';
      }
      return 'tik-tok...What are you waiting for?';
    },
  },
  data() {
    return {
      advices: [],
      addAdviceForm: {
        title: '',
        author: '',
        verified: [],
        tags: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getAdvices() {
      const path = 'http://localhost:5000/advices';
      axios.get(path)
        .then((res) => {
          this.advices = res.data.advices;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addAdvice(payload) {
      const path = 'http://localhost:5000/advices';
      axios.post(path, payload)
        .then(() => {
          this.getAdvices();
          this.message = 'Nice catch!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getAdvices();
        });
    },
    initForm() {
      this.addAdviceForm.title = '';
      this.addAdviceForm.author = '';
      this.addAdviceForm.verified = [];
      this.addAdviceForm.tags = [];
    },
    // above there is 2-way binding, below: actions after form submit
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addAdviceModal.hide();
      let verified = false;
      if (this.addAdviceForm.verified[0]) verified = true;
      const payload = {
        title: this.addAdviceForm.title,
        author: this.addAdviceForm.author,
        verified,
        tags: this.addAdviceForm.tags,
      };
      // Call `add` method with generated args
      this.addAdvice(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addAdviceModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getAdvices();
  },
};
</script>

