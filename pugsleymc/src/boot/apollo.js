import ApolloClient from 'apollo-boost'
import VueApollo from 'vue-apollo'

// "async" is optional
export default async ({ app, Vue }) => {
  const apolloClient = new ApolloClient({
    // You should use an absolute URL here
    // uri: 'http://pugsley.herokuapp.com/graphql'
    // uri: 'http://127.0.0.1:8000/graphql/'
    uri: process.env.GRAPHQL_URI
  })
  const apolloProvider = new VueApollo({
    defaultClient: apolloClient
  })
  Vue.use(VueApollo)
  app.apolloProvider = apolloProvider
}
