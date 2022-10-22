<template>
    <div id="main-container" class="mx-auto py-3 pb-0 border-dark
      border-bottom border-end rounded text-white"
      style="background-color:#326D86;text-shadow:1px 1px black">
      <h1 class="mb-3 text-center">Anagram Hunt</h1>
      <div v-if="screen === 'config'" id="config-container" class="mb-5 pb-5 mx-3">
        <!-- eslint-disable-next-line -->
        <SelectInput :currentValue="wordLength" label="Word Length" id="word-length"
          v-model:currentValue="wordLength" :options="numbers" />
        <ol class="mb-4" style="text-shadow:none">
          <li>Choose Word Length</li>
          <li>Press <strong>Play!</strong></li>
          <li>How Many Anagrams can you find in a minute?</li>
        </ol>
        <PlayButton @play-button-click="play"/>
      </div>
      <div v-else-if="screen === 'play'" id="game-container" class="text-center mx-3">
        <transition name="slide">
          <template v-if="timeLeft === 0">
            <div>
              <h2>Time's Up!</h2>
              <strong class="big">You Got</strong>
              <div class="huge">{{score}}</div>
              <strong class="big">Anagrams</strong>
              <button type="button" class="form-control btn btn-primary mt-4 mb-1"
                @click="restart()">
                  Play again with same settings
              </button>
              <button type="button" class="form-control btn btn-secondary"
                @click="config()">
                  Change Settings
              </button>
            </div>
          </template>
        </transition>
        <transition name="slide-right">
          <template v-if="timeLeft > 0">
            <div class="pt-3">
              <div id="scoreboard" class="row border-bottom py-2 mx-2" style="font-size:1.1rem">
                <div class="col text-start">
                  <Score :score="score" />
                </div>
                <div class="col text-end">
                  <Timer :timeLeft="timeLeft" />
                </div>
              </div>
              <div id="word">
                <Word :word="chosenWord" :wordsLeft="wordsLeft" />
              </div>
              <div id="user-input-container" class="m-2">
                <input id="user-input" ref="inputField" type="text" v-model.trim="userInput" autocomplete="off"
                  placeholder="type here" @keyup.enter="checkAnswered" class="w-75 p-2" autofocus/>
              </div>
              <div id="list">
                <ol class="py-0 px-4 m-0 mb-3 fs-5">
                  <li v-for="item in items" :key="item">{{item}}</li>
                </ol>
              </div>
            </div>
          </template>
        </transition>
      </div>
    </div>
</template>
<style>
	main {
		background-image: url('../../../../../../static/images/lettercloud_wd_cmp.png');
		background-size: 125vh;
	}
</style>
<script>
  import SelectInput from './SelectInput';
  import PlayButton from './PlayButton';
  import Score from './Score';
  import Timer from './Timer';
  import Word from './Word';
  import anagrams from '../../anagrams';

  export default {
    name: 'Main-El',
    components: {
      SelectInput,
      PlayButton,
      Score,
      Timer,
      Word,
    },

    data: function() {
      return {
        wordLength: '5',
        screen: 'config',
        score: 0,
        gameLength: 60,
        timeLeft: 0,
        userInput: '',
        anagrams: anagrams,
        bigArray: [],
        bigArrayStore: [],
        chosenWord: '',
        items: [],
				title_id: 2,
      }
    },

    methods: {

      config() {
        this.screen = "config";
      },

      play() {
        this.screen = "play";
        this.newWord();
        this.startTimer();
      },

      focusOnInputField() {
        this.$nextTick(() => {
          const inputFieldRef = this.$refs.inputField;
          inputFieldRef.focus();
        })
      },

      getRandWord() {
        this.bigArray = anagrams[this.wordLength];
        if (this.bigArray.length === this.bigArrayStore.length) {
          this.timeLeft = 1;
          this.bigArrayStore = [];
          return false;
        }
        let randNum2 = Math.floor(Math.random() * this.bigArray.length);
        this.smallArray = this.bigArray[randNum2];
        let randNum3 = Math.floor(Math.random() * this.smallArray.length);
        this.chosenWord = this.smallArray[randNum3];
        let bigString = JSON.stringify(this.bigArrayStore);
        if (bigString.includes(this.chosenWord)) {
          this.getRandWord();
          return;
        }
        console.log(this.smallArray);
      },

      newWord() {
        this.getRandWord();
        this.wordsLeft = this.smallArray.length - 1;
        setTimeout(() => {
          this.items.length = 0;
        }, 500);
      },

      checkAnswered() {
        for (let item in this.items) {
          if (this.items[item].includes(this.userInput.toLowerCase())) {
            this.userInput = '';
            return;
          }
        }
        if (this.userInput.toLowerCase() === this.chosenWord) {
          this.userInput = '';
        } else if (this.smallArray.includes(this.userInput.toLowerCase())) {
          this.correctAnswer();
        }
        if ((this.smallArray.length - 1) === this.items.length) {
          this.wordDone();
        }
        this.userInput = '';
      },

      correctAnswer() {
        this.items.push(this.userInput.toLowerCase());
        this.wordsLeft--;
        this.score++;
      },

      sliceArray() {
        let pos = this.bigArray.indexOf(this.smallArray)
        this.bigArrayStore.push(this.bigArray.slice(pos, pos + 1));
      },

      wordDone() {
        this.sliceArray();
        this.newWord();
      },

      async recordScore() {
          const payload = {
              "word_length": this.wordLength,
              "score": this.score,
              "game": "Anagram Hunt",
          };

          console.log(payload)
          const response = (await this.axios.post("../record-score/", payload)).data;
          console.log(response);
      },

      startTimer() {
        this.timeLeft = this.gameLength;
        if (this.timeLeft > 0) {
          this.timer = setInterval(() => {
            this.timeLeft--;
            if (this.timeLeft === 0) {
							this.userInput = '';
							this.recordScore();
              clearInterval(this.timer);
            }
          }, 1000)
        }
      },

      restart() {
				this.score = 0;
        this.startTimer();
        this.newWord();
        this.focusOnInputField();
      },

    },

    computed: {
      numbers: function() {
        const numbers = [];
        for (let number = 5; number <= 8; number++) {
          numbers.push([number, number]);
        }
        return numbers;
      },
    }
  }
</script>
<style scoped>

  #main-container {
  /* position: relative; */
  /* margin: auto; */
  height: 500px;
  width: 425px;
  }

  ol > li {
    margin: .5em 0;
  }

  #list {
    height: 200px;
  }

  .big {
    font-size: 1.5rem;
  }

  .huge {
    font-size: 5em;
  }

  .slide-leave-active,
  .slide-enter-active {
    transition: 1s;
    width: auto;
    height: 0;
  }

  .slide-enter-from {
    transform: translate(-100%, 0);
    transition: opacity .5s;
  }

  .slide-leave-to {
    opacity:0;
    transform: translate(100%, 0);
  }

  .slide-right-leave-active,
  .slide-right-enter-active {
    transition: 1s;
  }

  .slide-right-enter-from {
    transform: translate(100%, 0);
    transition: opacity .5s;
  }

  .slide-right-leave-to {
    width: 325px;
    opacity:0;
    transform: translate(-100%, 0);
  }

  @media (max-width:600px) {
    /* #game-container {
      position: absolute;
      justify-content: center;
      width: 95vw;
    } */

    .slide-leave-active,
    .slide-enter-active {
      transition: .5s;
      width: auto;
      height: 0;
    }

    .slide-right-leave-active,
    .slide-right-enter-active {
      transition: .5s;
      width: 85vw;
    }
  }
</style>