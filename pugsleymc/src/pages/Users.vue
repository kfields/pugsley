<template>
  <q-page padding>
    <div style="width: 500px; max-width: 90vw;">
      <q-list>
        <q-item v-for="edge in allUsers.edges" :key="edge.id" :to="`/users/${edge.node.id}`">
          <q-item-section avatar>
            <q-icon name="mdi-account" inverted color="grey-6" />
          </q-item-section>
          <q-item-section>
            {{ edge.node.firstName }} {{ edge.node.lastName }}
          </q-item-section>
      </q-item>
      </q-list>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import { UiMixin, PageMixin } from 'src/mixins'

import gql from 'graphql-tag'
const userQuery = gql`
query userQuery {
  allUsers {
    edges {
      node {
        id
        firstName
        lastName
        username
      }
    }
  }
}
`
export default {
  name: 'Users',
  mixins: [ UiMixin, PageMixin ],

  data () {
    return {
      title: 'Users'
    }
  },
  apollo: {
    allUsers: {
      query: userQuery,
      prefetch: false
    }
  }
}
</script>
