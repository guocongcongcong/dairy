const bill = {
    state: {
       info:{
        name: "",
        total: "",
        rest: "",
        owe: ""
      },
      settings:{
        startDate:"",
        endDate:"",
        enterDate:"",
        singleMoney:"",
        rate:"",
        billsLength:"",
        expenditure:[]
      },
    //   tableData: [
    //     {
    //       date: "",
    //       total: "",
    //       expenditure: "",
    //       accumulation: "",
    //       repayment: ""
    //     }
    //   ],
    },
    mutations: {
        getBillInfo(state,sums) {
            state.info.name = sums[0];
            state.info.total = sums[1];
            state.info.rest = sums[2];
            state.info.owe = sums[3];
          },
        getSettings(state,info){
            state.settings = info;
        },
        // uploadDate(state,tableData){
        //     state.tableData = tableData;
        // }
    }
}

export default bill
