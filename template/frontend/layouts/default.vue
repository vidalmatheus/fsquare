<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      mini-variant
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-tooltip right>
              <template #activator="{ on, attrs }">
                <v-icon
                  v-bind="attrs"
                  v-on="on"
                >
                  {{ item.icon }}
                </v-icon>
              </template>
              <span>{{ item.title }}</span>
            </v-tooltip>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-layout row>
        <v-flex xs4>
          <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        </v-flex>
        <v-flex row xs4 class="text-center align-self-center">
          <v-row>
            <v-col class="text-right pr-1">
              <router-link to="/">
                <v-avatar
                  rounded
                  size="32"
                >
                  <v-img
                    src="/icon.png"
                    alt="F-square"
                    width="32"
                    height="32"
                  />
                </v-avatar>
              </router-link>
            </v-col>
            <v-col class="text-left pl-1">
              <v-toolbar-title>
                F-square
              </v-toolbar-title>
            </v-col>
          </v-row>
        </v-flex>
        <v-flex xs4 class="text-right align-self-center">
          <v-btn
            v-if="!loggedIn"
            text
            ripple
            @click="openLoginDialog()"
          >
            Login
          </v-btn>
          <v-menu
            v-else
            offset-y
          >
            <template #activator="{ on, attrs }">
              <v-btn
                class="ma-0 ml-5"
                icon
                v-bind="attrs"
                v-on="on"
              >
                <v-avatar size="36px">
                  <img :src="loggedUser.avatar">
                </v-avatar>
              </v-btn>
            </template>
            <v-card class="no-padding">
              <v-list two-line>
                <v-list-item>
                  <v-list-item-avatar>
                    <img :src="loggedUser.avatar">
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ loggedUser.first_name }} {{ loggedUser.last_name }}
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      {{ loggedUser.email }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <v-divider />
              <v-list two-line>
                <v-list-item @click.stop="rightDrawer = !rightDrawer">
                  <v-list-item-content>
                    <v-list-item-title>
                      Notificações
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item @click="logout()">
                  <v-list-item-content>
                    <v-list-item-title>Log out</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-menu>
        </v-flex>
      </v-layout>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
    >
      <v-list>
        <v-list-item>
          <v-list-item-action>
            <v-icon light @click="right = !right">
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch side</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-footer
      :absolute="!fixed"
      app
    >
      <v-spacer />
      <span>F-square &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
    <LoginDialog ref="LoginDialog" />
    <Toast />
  </v-app>
</template>

<script>
import api from '~api'

export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Home',
          to: '/'
        },
        {
          icon: 'mdi-account-box',
          title: 'Who am I?',
          to: '/whoami'
        }
      ],
      right: true,
      rightDrawer: false,
      title: 'fSquare'
    }
  },
  computed: {
    loggedIn () {
      return this.$store.getters['auth/loggedIn']
    },
    loggedUser () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    openLoginDialog () {
      this.$refs.LoginDialog.open()
    },
    async logout () {
      try {
        await api.auth.logout()
        this.$store.commit('auth/setCurrentUser', null)
        this.$store.commit('toast/open', {
          message: 'See ya!'
        })
        if (this.$route.name !== 'index') {
          this.$router.push({ name: 'index' })
        }
      } catch (err) {
        this.$store.commit('toast/open', {
          message: err,
          color: 'error'
        })
      }
    }
  }
}
</script>
