<template>
  <q-page padding class="fields">
      <q-input outlined autocomplete="title" v-model="post.title" label="Title" />
      <q-field outlined label="Body" stack-label @click.native="editBody()">
        <template v-slot:control>
          <div class="self-center full-width no-outline" tabindex="0">{{stripTags(post.body)}}</div>
        </template>
      </q-field>
  </q-page>
</template>

<script>
import { UiMixin, PageMixin } from 'src/mixins'
import Toolbar from './Toolbar'

import gql from 'graphql-tag'
const postQuery = gql`
query postQuery($id: ID!) {
  post(id: $id) {
    title
    slug
    body
  }
}
`
export default {
  mixins: [ UiMixin, PageMixin ],
  props: ['id'],
  components: {
  },
  apollo: {
    post: {
      query: postQuery,
      variables () {
        return {
          id: this.postId
        }
      }
    }
  },
  data () {
    return {
      title: 'Page',
      postId: this.$route.params.id
    }
  },
  mounted () {
  },
  beforeDestroy () {
  },
  methods: {
    editBody () {
      this.setEdited({ object: this.post, prop: 'body' })
      this.$router.push('/html')
    },
    save () {
      this.$apollo.mutate({
        // Query
        mutation: gql`mutation ($id: ID!, $title: String, $body: String) {
          updatePost(id: $id, title: $title, body: $body) {
            ok
          }
        }`,
        // Parameters
        variables: {
          id: this.id,
          title: this.post.title,
          body: this.post.body
        }
      })
      this.$q.notify('Page Saved')
    },
    onSwitch () {
      this.setPage(this)
      this.setToolbar(Toolbar)
    },
    stripTags (str) {
      if ((str === null) || (str === '')) {
        return ''
      } else {
        str = str.toString()
        return str.replace(/<[^>]*>/g, '')
      }
    }
  }
}
</script>
