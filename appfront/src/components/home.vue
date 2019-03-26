<template>
  <div>
    <el-steps :active="active" finish-status="success" class="step_bar">
      <el-step title="步骤 1" description="ID校验"></el-step>
      <el-step title="步骤 2" description="取流设置"></el-step>
      <el-step title="步骤 3" description="算法配置"></el-step>
    </el-steps>

    <div class="id_test" v-if="active === 0">
      <el-select v-model="value" placeholder="请选择你要配置的终端" @change="id_change">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <div class="input_id">
        <el-row style="margin-top: 40px">
          <el-input v-model="res_id" placeholder="请输入饭店ID" style="width: 200px" :disabled="input_id"></el-input>
          <el-button @click="jiaoyan">校验</el-button>
        </el-row>
      </div>
      <div style="text-align: center; margin-top: 40px">
        <el-row>饭店名称：{{res_name}}</el-row>
      </div>
    </div>
    <div class="setting" v-if="active === 2">

    </div>
    <div class="algorithm" v-if="active === 3">

    </div>
    <div style="text-align: center; margin-top: 40px">
      <el-button style="margin-top: 12px; align-items: center" @click="next" :disabled="next_flag">下一步</el-button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "home",
    data() {
      return {
        active: 0,
        options: [{
          value: '终端1',
          label: '终端1'
        }, {
          value: '终端2',
          label: '终端2'
        }, {
          value: '终端3',
          label: '终端3'
        }, {
          value: '终端4',
          label: '终端4'
        }, {
          value: '终端5',
          label: '终端5'
        }, {
          value: '终端6',
          label: '终端6'
        }, {
          value: '终端7',
          label: '终端7'
        }, {
          value: '终端8',
          label: '终端8'
        }],
        value: '',
        res_id: '',
        input_id: true,
        res_name: '',
        next_flag: true
      }
    },
    methods: {
      next() {
        if (this.active++ > 2) this.active = 0;
      },

      id_change() {
        console.log(this.value.length)
        if (this.value.length == 0) {
          this.input_id = true
        } else {
          this.input_id = false
        }
      },

      jiaoyan() {
        var that = this
        if (this.res_id.length == 0) {
          that.$message({
            message: '请输入饭店id',
            type: 'warning'
          });
        } else {
          this.$http.get('http://127.0.0.1:8000/api/find_company_id?res_id=' + that.res_id)
            .then((response) => {
              var res = JSON.parse(response.bodyText)['name']
              if (res.length == 0) {
                that.$message({
                  message: '校验失败，请检查后重试',
                  type: 'error'
                });
              } else {
                that.$message({
                  message: '校验成功',
                  type: 'success'
                });
                this.res_name = res
                this.next_flag = false
              }
            })
        }
      }
    }
  }
</script>

<style scoped>
  .step_bar {
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 30px;
  }

  .id_test {
    margin-top: 50px;
    text-align: center;
  }
</style>
