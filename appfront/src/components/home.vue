<template>
  <div>
    <el-container style="height: 100vh; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1','2', '3']" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>终端配置</template>
            <el-menu-item-group>
              <template slot="title"></template>
              <el-menu-item index="/map">终端地图</el-menu-item>
              <el-menu-item index="/home">算法配置</el-menu-item>
            </el-menu-item-group>
            <el-menu-item index="1-3">删除终端</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>数据管理</template>
            <el-menu-item index="2-1">报警信息</el-menu-item>
            <el-menu-item index="/statistic_chart">统计图表</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i>视频查看</template>
            <el-menu-item-group>
              <template slot="title"></template>
              <el-menu-item index="3-1">实时浏览</el-menu-item>
              <el-menu-item index="3-2">警报视频</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>admin</span>
        </el-header>

        <el-main>
          <el-steps :active="active" finish-status="success" class="step_bar">
            <el-step title="步骤 1" description="选择终端"></el-step>
            <el-step title="步骤 2" description="ID校验"></el-step>
            <el-step title="步骤 3" description="取流设置"></el-step>
            <el-step title="步骤 4" description="算法配置"></el-step>
          </el-steps>
          <div class="id_test" v-if="active === 0">
            <el-dialog title="配置情况" :visible.sync="PeizhiVisible">
              <el-table :data="peizhiData">
                <el-table-column property="res_id" label="饭店ID" width="110"></el-table-column>
                <el-table-column property="res_name" label="饭店名称" width="110"></el-table-column>
                <el-table-column property="cam_id" label="摄像头编号" width="110"></el-table-column>
                <el-table-column property="maozi" label="帽子" width="110"></el-table-column>
                <el-table-column property="kouzhao" label="口罩" width="110"></el-table-column>
                <el-table-column property="mouse" label="老鼠" width="110"></el-table-column>
                <el-table-column property="picture" label="抓图" width="110"></el-table-column>
              </el-table>
            </el-dialog>
            <el-dialog
              title="提示"
              :visible.sync="centerDialogVisible"
              width="30%"
              center>
              <span style="text-align: center">是否重新配置终端算法，点击确定之后算法将会重置</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="centerDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="chongxinpeizhi">确 定</el-button>
              </span>
            </el-dialog>
            <el-table
              :data="tableData"
              style="width: 60vw; margin:auto">
              <el-table-column
                label="终端号"
                width="300">
                <template slot-scope="scope">
                  <i class="el-icon-info"></i>
                  <span style="margin-left: 10px">{{ scope.row.terminal }}</span>
                </template>
              </el-table-column>
              <el-table-column
                label="配置情况"
                width="300">
                <template slot-scope="scope">
                  <el-tag size="medium">{{ scope.row.detail }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button
                    size="mini"
                    @click="handlechakan(scope.$index, scope.row)"
                    :disabled="scope.row.peizhi">查看配置
                  </el-button>
                  <el-button
                    size="mini"
                    type="danger"
                    @click="handlepeizhi(scope.$index, scope.row)">配置
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div class="id_test" v-if="active === 1">
            <div class="input_id">
              <el-row style="margin-top: 150px">
                <el-input v-model="res_id" placeholder="请输入饭店ID" style="width: 200px"></el-input>
                <el-button @click="jiaoyan">校验</el-button>
              </el-row>
            </div>
            <div style="text-align: center; margin-top: 40px">
              <el-row>饭店名称：{{res_name}}</el-row>
            </div>
            <el-row style="margin-top: 40px">
              <el-button style="margin-top: 12px;" @click="previous" :disabled="pre_flag">上一步
              </el-button>
              <el-button style="margin-top: 12px;" @click="next" :disabled="next_flag">下一步
              </el-button>
            </el-row>
          </div>
          <div class="setting" v-if="active === 2">
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

            <el-dialog title="信息配置" :visible.sync="dialogFormVisible" width="500px">
              <el-form :model="login_info">
                <el-form-item label="用户名: ">
                  <el-input v-model="login_info.name" autocomplete="off" style="width: 300px"></el-input>
                </el-form-item>
                <el-form-item label="密码: ">
                  <el-input v-model="login_info.password" autocomplete="off" style="width: 300px"></el-input>
                </el-form-item>
                <el-form-item label="ID: ">
                  <el-input v-model="login_info.ip" autocomplete="off" style="width: 300px"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="login_confirm">确 定</el-button>
              </div>
            </el-dialog>
            <div style="margin-right: auto;  margin-left: auto;width:510px;  height: 400px; margin-top: 50px">
              <el-transfer v-model="cam_id" :data="cam_data" style="text-align: left" :titles="titles"
                           @change="cam_id_change"></el-transfer>
            </div>

            <el-dialog title="RTSP" :visible.sync="rtsp_show">
              <el-table :data="gridData">
                <el-table-column property="rtsp" label="rtsp"></el-table-column>
              </el-table>
            </el-dialog>

            <el-row style="text-align: center; margin-top: 0px">
              <el-button @click="cam_id_confirm">确定</el-button>
              <el-button @click="see_rtsp">查看rtsp</el-button>
            </el-row>

            <el-row style="margin-top: 40px; margin-bottom: 40px">
              <el-button style="margin-top: 12px;" @click="previous" :disabled="pre_flag">上一步
              </el-button>
              <el-button style="margin-top: 12px;" @click="next" :disabled="next_flag">下一步
              </el-button>
            </el-row>
          </div>
          <div class="algorithm" v-if="active === 3">
            <el-form :inline="true" :model="formInline" v-for="form in formInline" :key="form" class="demo-form-inline">
              <el-form-item :label="form.cam_id">
              </el-form-item>
              <el-form-item label="帽子">
                <el-checkbox v-model="form.maozi_checked"></el-checkbox>
              </el-form-item>
              <el-form-item label="口罩">
                <el-checkbox v-model="form.kouzhao_checked"></el-checkbox>
              </el-form-item>
              <el-form-item label="老鼠">
                <el-checkbox v-model="form.mouse_checked"></el-checkbox>
              </el-form-item>
              <el-form-item label="抓图">
                <el-checkbox v-model="form.picture_checked"></el-checkbox>
              </el-form-item>
            </el-form>
            <el-button @click="suanfa_confirm">配置</el-button>
            <el-button @click="wancheng_confirm" :disabled="suanfa">完成</el-button>
          </div>

          <!--<div style="text-align: center; margin-top: 40px">-->
          <!--<el-button style="margin-top: 12px; align-items: center" @click="next" :disabled="next_flag">下一步</el-button>-->
          <!--</div>-->
        </el-main>

        <el-footer style="text-align: center; font-size: 10px">
          版权所有 © 上海大学
        </el-footer>
      </el-container>
    </el-container>

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
            label: `摄像头 ${i + "01"}`
          });
        }
        return cam_data;
      };
      return {
        active: 0,
        value: '',  //要配置的终端
        res_id: '',  //饭店的id
        res_name: '',  //饭店的名称
        next_flag: false,  //第一步“下一步”按钮的标志位
        tableData: [{
          terminal: '终端一',
          detail: '未配置',
          peizhi: false
        }, {
          terminal: '终端二',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端三',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端四',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端五',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端六',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端七',
          detail: '未配置',
          peizhi: true
        }, {
          terminal: '终端八',
          detail: '未配置',
          peizhi: true
        },],
        cam_value: '',  //选中的相机类型
        cam_flag: true,  //标志是否已经选择相机
        dialogFormVisible: false,  //是否隐藏弹出的登录界面
        login_info: {  //用户输入的登录信息
          name: '',
          password: '',
          ip: ''
        },
        cam_data: generateData(),  //可以选择的摄像头编号
        cam_id: [],  //选择的摄像头编号
        titles: ['可选摄像头编号', '已选摄像头编号'],  //选择摄像头部件的标题
        rtsp_show: false,  //rtsp显示窗口是否显示
        gridData: [],  //rtsp窗口显示的数据
        formInline: [],
        PeizhiVisible: false,
        peizhiData: [],
        centerDialogVisible: false,
        terminal_id: '',
        cam_options: [{
          value: '海康',
          label: '海康'
        }, {
          value: '其他',
          label: '其他'
        }],
        suanfa: true,
      }
    },
    methods: {
      next() {  //点击下一步
        if (this.active++ > 2) this.active = 0;
      },
      previous(){
        if (this.active -- < 0) this.active = 0;
      },
      chongxinpeizhi() {
        let that = this;
        that.centerDialogVisible = false;
        $.ajax({
          url: "api/del_rtsp_idconfig_by_terminal",
          dataType: "json",
          data: {
            terminal_id: this.terminal_id
          },
          success: function (data) {
            if (data['res'] === "yes") {
              // that.next()  //正式环境需取消注释
            } else {
              console.log(response)
              that.$message({
                message: '网络错误，请重试',
                type: 'warning'
              });
            }
          }
        })
        that.next() // 测试用
        // that.$http.get('http://127.0.0.1:8000/api/del_rtsp_idconfig_by_terminal?terminal_id=' + that.terminal_id)
        //   .then((response) => {
        //     if (response.body['res'] === 'yes') {
        //       // that.next()  //正式环境需取消注释
        //     } else {
        //       console.log(response)
        //       that.$message({
        //         message: '网络错误，请重试',
        //         type: 'warning'
        //       })
        //     }
        //   });
        // that.next() // 测试用
      },
      handlechakan(index, row) {
        this.PeizhiVisible = true;
        let that = this;
        this.$http.get('http://127.0.0.1:8082/api/search_idconfig_by_terminal?terminal=' + row.terminal)
          .then((response) => {
            console.log(response);
            that.peizhiData = response.body
          });
        console.log(index, row.terminal);
      },
      handlepeizhi(index, row) {
        console.log(index, row);
        this.centerDialogVisible = true;
        this.terminal_id = row.terminal
      },
      id_change() {  //饭店的id发生变化
        console.log(this.value.length)
        if (this.value.length === 0) {
          this.input_id = true
        } else {
          this.input_id = false
        }
      },

      jiaoyan() {  //校验按钮
        let that = this;

        if (this.res_id.length === 0) {
          that.$message({
            message: '请输入饭店id',
            type: 'warning'
          });
        } else {
          this.$http.get('http://127.0.0.1:8082/api/find_company_id?res_id=' + that.res_id)
            .then((response) => {
              var res = JSON.parse(response.bodyText)['name']
              if (res.length === 0) {
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

      login_confirm() {  //登录rtsp的函数
        var that = this
        if (this.login_info.name === '' || this.login_info.ip === '' || this.login_info.password === '') {
          that.$message({
            message: '请填充所有的选项哦',
            type: 'warning'
          });
        } else {
          this.dialogFormVisible = false
        }

      },
      cam_id_confirm() {
        var that = this;
        if (that.cam_id.length === 0) {
          that.$message({
            message: '请至少选择一个摄像头哦',
            type: 'warning'
          })
        } else if (that.cam_id.length > 8) {
          that.$message({
            message: '最多选择八个摄像头哦',
            type: 'warning'
          })
        } else {
          var res = ""
          for (var i = 0; i < that.cam_id.length; i++) {
            console.log(that.cam_id[i])
            var rtsp = "rtsp://" + that.login_info.name + ":" + that.login_info.password + "@" + that.login_info.ip + ":554/streaming/channels/" + that.cam_id[i] + "?transportmode=unicast?"
            that.$http.get('http://127.0.0.1:8082/api/add_rtsp?id=' + that.res_id + '&&res_name=' + that.res_name + "&&camid=" + that.cam_id[i] + "&&rtsp=" + rtsp + "&&cam_name=" + that.cam_value + "&&terminal_id=" + that.terminal_id)
              .then((response) => {
                if (response['res'] === 'ok') {
                  res = response['res']

                }
              })
          }
          if (res === "") {
            that.$message({
              message: '添加成功',
              type: 'success'
            })
          }

        }
      },

      see_rtsp() {  //点击查看rtsp按钮触发的事件
        var that = this;
        that.$http.get('http://127.0.0.1:8082/api/see_rtsp?res_id=' + that.res_id)
          .then((response) => {
            console.log(response)
            for (var i = 0; i < response.body.length; i++) {
              console.log(i)
              console.log(response.body[i])
              that.gridData.push({'rtsp': response.body[i]['rtsp']})
            }
          });
        that.rtsp_show = true
      },

      cam_id_change() {
        var that = this;
        console.log(that.formInline)
        that.formInline = [];
        for (var i = 0; i < that.cam_id.length; i++) {
          that.formInline.push({
            'cam_id': that.cam_id[i],
            'maozi_checked': false,
            'kouzhao_checked': false,
            'mouse_checked': false,
            'picture_checked': false
          })
        }
      },

      suanfa_confirm() {
        let that = this;
        var channel = "";
        for (var i = 0; i < that.formInline.length; i++) {
          channel += "C" + that.formInline[i]['cam_id'] + "S";
          if (that.formInline[i]['maozi_checked'] === true) {
            channel += "1107000000";
          } else {
            channel += "1007000000";
          }
          if (that.formInline[i]['kouzhao_checked'] === true) {
            channel += "2107000000";
          } else {
            channel += "2007000000";
          }
          if (that.formInline[i]['mouse_checked'] === true) {
            channel += "3100000500";
          } else {
            channel += "3000000500";
          }
          if (that.formInline[i]['picture_checked'] === true) {
            channel += "4107000000";
          } else {
            channel += "4007000000";
          }
        }
        that.$http.get('http://127.0.0.1:8082/api/add_idconfig?res_id=' + that.res_id + "&&config=" + channel + "&&capturedserver=00&&interval=3600000&&terminal_id=" + that.terminal_id)
          .then((response) => {
            console.log(response);
            if (response.body['res'] === 'ok') {
              that.$message({
                message: '配置成功',
                type: 'success'
              });
              that.suanfa = false;
            }
          });

      },
      wancheng_confirm(){
        location.reload()
      },

    },
    mounted() {
      let that = this;
      this.$http.get('http://127.0.0.1:8082/api/search_terminal')
        .then((response) => {
          response = response.body
          console.log(response)
          console.log(response.length)
          for (var i = 0; i < response.length; i++) {
            console.log(response)
            for (var j = 0; j < that.tableData.length; j++) {
              if (that.tableData[j].terminal === response[i]['terminal_id']) {
                console.log(that.tableData[j].terminal)
                that.tableData[j].detail = '已配置'
                that.tableData[j].peizhi = false
              }
            }
          }
        })
    }
  }
</script>

<style scoped>
  .step_bar {
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 30px;
  }

  .id_test, .setting, .algorithm {
    margin-top: 50px;
    text-align: center;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>
