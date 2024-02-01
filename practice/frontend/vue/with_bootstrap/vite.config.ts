import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

const config = defineConfig({
  plugins: [vue()],
})

config.resolve = {
  alias:{
    '@': path.resolve(__dirname, './src'),
  }
}

config.css = {
    preprocessorOptions:{
      scss: {
        additionalData: `
          @import "@/style/_variables.scss";
        `,
      }
    }
}

export default config