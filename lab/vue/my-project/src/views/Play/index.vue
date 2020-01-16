<template>
  <div >
    <v-container>
      <v-responsive :aspect-ratio="16/9">
        <v-card-text>
          <video v-bind="video.type" controls>
            <source :src="video.sources.src" :type="video.sources.type">
          </video>
        </v-card-text>
      </v-responsive>
    </v-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      video: {
        type: {
          height: "550",
          maxHeight: "900px",
          maxWidth: "1600px",
          minHeight: "90px",
          minWidth: "160px",
          width: "1100px"
        },
        sources: {
          src: "static/Top 10 Best EDC Multi Tools.mp4",
          type: "video/mp4"
        },
        options: {
          autoplay: true,
          volume: 0.6,
          poster: "static/logo.png"
        }
      }
    };
  }
};
</script>

