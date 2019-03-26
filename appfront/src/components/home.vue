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
    <div class="setting" v-if="active === 1">
      <el-row>
        <el-select v-model="cam_value" placeholder="请选择摄像头类型" @change="cam_change">
          <el-option
            v-for="item in cam_options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-button @click="cam_login" :disabled="cam_flag">确定</el-button>
      </el-row>

      <el-dialog title="信息配置" :visible.sync="dialogFormVisible">
        <el-form :model="login_info">
          <el-form-item label="用户名: ">
            <el-input v-model="login_info.name" autocomplete="off" style="width: 300px"></el-input>
          </el-form-item>
          <el-form-item label="密码: ">
            <el-input v-model="login_info.password" autocomplete="off" style="width: 300px"></el-input>
          </el-form-item>
          <el-form-item label="ID: ">
            <el-input v-model="login_info.id" autocomplete="off" style="width: 300px"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="login_confirm">确 定</el-button>
        </div>
      </el-dialog>
      <div style="margin-right: auto;  margin-left: auto;width:550px;  height: 400px; margin-top: 50px">
        <el-transfer v-model="cam_id" :data="cam_data" style="text-align: left"></el-transfer>
      </div>
    </div>
    <div class="algorithm" v-if="active === 2">

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
      const generateData = _ => {
        const cam_data = [];
        for (let i = 1; i <= 31; i++) {
          cam_data.push({
            key: i + "01",
            label: `摄像机 ${i + "01"}`
          });
        }
        return cam_data;
      };
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
        value: '',  //要配置的终端
        res_id: '',  //饭店的id
        input_id: true,  //是否已经输入id
        res_name: '',  //饭店的名称
        next_flag: false,  //第一步“下一步”按钮的标志位

        cam_options: [{  //相机列表
          value: '海康',
          label: '海康'
        }, {
          value: '其他',
          label: '其他'
        }],
        cam_value: '',  //选中的相机类型
        cam_flag: true,  //标志是否已经选择相机
        dialogFormVisible: false,
        login_info: {
          name: '',
          password: '',
          id: ''
        },
        formLabelWidth: '200px',
        cam_data: generateData(),
        cam_id: [1, 4]
      }
    },
    methods: {
      next() {  //点击下一步
        if (this.active++ > 2) this.active = 0;
      },

      id_change() {  //饭店的id发生变化
        console.log(this.value.length)
        if (this.value.length == 0) {
          this.input_id = true
        } else {
          this.input_id = false
        }
      },

      jiaoyan() {  //校验按钮
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
      },

      cam_change() {
        this.cam_flag = false
      },

      cam_login() {
        this.dialogFormVisible = true
      },

      login_confirm() {
        var that = this
        if (this.login_info.name == '' || this.login_info.id == '' || this.login_info.password == '') {
          that.$message({
            message: '请填充所有的选项哦',
            type: 'warning'
          });
        } else {
          this.dialogFormVisible = false
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

  .id_test, .setting {
    margin-top: 50px;
    text-align: center;
  }
</style>
