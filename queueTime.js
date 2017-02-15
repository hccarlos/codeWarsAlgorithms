function queueTime(customers, n) {
  var reg = [];
  var totalTime = 0;
  do {
    for (let i = 0; i < reg.length; i++){
      reg[i]--;
      if(reg[i] < 1 ){
      reg.splice(i, 1);
      }
    }
    for (let i = reg.length; i < n; i++){
      if (customers.length > 0 ){
        reg.push(customers.pop());
      }
    }
    totalTime++;
  } while(customers.length > 0 && reg.length > 0);
  return totalTime;
}
queueTime([5, 10, 4], 4);
