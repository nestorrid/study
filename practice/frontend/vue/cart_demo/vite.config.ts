import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve:{
    alias:{
      '@': path.resolve(__dirname, './src'),
    }
  },
  css:{
    preprocessorOptions:{
      scss: {
        additionalData: `
          @import "@/style/_variables.scss";
          @import "@/style/_base.scss";
          @import "@/style/_functions.scss";
          @import "@/style/_mixin.scss";
          @import "@/style/_frames.scss";
        `,
      }
    }
  }
})
