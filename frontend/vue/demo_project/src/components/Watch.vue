<script setup lang="ts">
import { ref, watch } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')
const img = ref(null)

// 可以直接侦听一个 ref
watch(question, async (newQuestion) => {
    if (newQuestion.indexOf('?') > -1) {
        answer.value = 'Thinking...'
        try {
            const res = await fetch('https://yesno.wtf/api')
            const json = (await res.json())
            answer.value = json.answer
            img.value = json.image

        } catch (error) {
            answer.value = 'Error! Could not reach the API. ' + error
        }
    }
})
</script>

<template>
    <h1>监听器Demo</h1>
    <p>
        Ask a yes/no question:
        <input v-model="question" />
    </p>
    <img v-if="img" :src="img" style="{width: 400;}" alt="answer" />
    <p>{{ answer }}</p>
</template>