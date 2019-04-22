<template>
  <q-toolbar>
    <q-btn
      flat
      dense
      round
      @click="$router.go(-1)"
    >
      <q-icon name="mdi-chevron-left" />
    </q-btn>
    <q-btn
      flat
      dense
      round
      @click="$router.push('/text')"
    >
      <q-icon name="mdi-language-html5" />
    </q-btn>
    <editor-menu-bar :editor="editor">
      <div class="menubar" slot-scope="{ commands, isActive }">

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bold() }"
          @click="commands.bold"
        >
          <q-icon name="mdi-format-bold" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
          <q-icon name="mdi-format-italic" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        >
          <q-icon name="mdi-format-strikethrough" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
          <q-icon name="mdi-format-underline" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code() }"
          @click="commands.code"
        >
          <q-icon name="mdi-code-tags" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.paragraph() }"
          @click="commands.paragraph"
        >
          <q-icon name="mdi-format-paragraph" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          <q-icon name="mdi-format-list-bulleted" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          <q-icon name="mdi-format-list-numbered" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.blockquote() }"
          @click="commands.blockquote"
        >
          <q-icon name="mdi-format-quote-close" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code_block() }"
          @click="commands.code_block"
        >
          <q-icon name="mdi-code-not-equal-variant" />
        </button>

        <button
          class="menubar__button"
          @click="commands.horizontal_rule"
        >
          <q-icon name="mdi-minus" />
        </button>

        <button
          class="menubar__button"
          @click="showImagePrompt(commands.image)"
        >
          <q-icon name="mdi-image" />
        </button>

        <button
          class="menubar__button"
          @click="commands.undo"
        >
          <q-icon name="mdi-undo" />
        </button>

        <button
          class="menubar__button"
          @click="commands.redo"
        >
          <q-icon name="mdi-redo" />
        </button>

      </div>
    </editor-menu-bar>

  </q-toolbar>
</template>

<script>
import UiMixin from 'src/mixins/ui'
import { EditorMenuBar } from 'tiptap'
export default {
  name: 'BasicToolbar',
  mixins: [ UiMixin ],
  props: [],
  components: {
    EditorMenuBar
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    showImagePrompt (command) {
      const src = prompt('Enter the url of your image here')
      if (src !== null) {
        command({ src })
      }
    }
  }
}
</script>
