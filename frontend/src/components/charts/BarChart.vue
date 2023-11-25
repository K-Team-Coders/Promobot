<template>
  <Bar :chart-data="chartData" :chart-options="chartOptions" />
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  props: {
    dataset: Object,
    label_name: String,
  },
  name: "BarChart",
  components: { Bar },
  // mounted() {
  //   console.log(this.dataset)
  //   let name_set = []
  //   let pos_set = []
  //   let neu_set = []
  //   let neg_set = []
  //   this.dataset.forEach(element => {
  //   name_set.push(element.cluster_name),
  //   pos_set.push( element.numPositive),
  //   neu_set.push( element.numNeutral),
  //   neg_set.push( element.numNegative)
  //   });
  //   this.chartData.labels = name_set
  //   this.chartData.datasets[0].data = pos_set
  //   this.chartData.datasets[1].data = neu_set
  //   this.chartData.datasets[2].data = neg_set
  // },
  computed:{
  },
  data() {
    return {
      chartData: {
        labels: Object.keys(this.dataset),

        datasets: [
       { data: Object.values(this.dataset),
      label: this.label_name,
      backgroundColor: '#f87979'
     } 
        ],
      },
      chartOptions: {
        stacked: true,
        maintainAspectRatio: false,
        scales: {
        x: {
          ticks: {
            autoSkip: true, // Отключает автоматическое пропускание labels
            maxRotation: 0, // Поворот labels на 90 градусов (можно указать другое значение)
            minRotation: 90, // Поворот labels на 90 градусов (можно указать другое значение)
          },
        },
      },
      },
      
    };
  },
};
</script>
