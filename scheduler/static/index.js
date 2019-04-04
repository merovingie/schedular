// const canvas = d3.select("canvas");
const svg = d3.select("svg");
const group = svg.append('g');
// d3.request("http://localhost:8000/json/forjs/")
// .header("Content-Type", "application/json")
// .post(function(data) {
//    console.log(data);
// });

d3.json('http://localhost:8000/json/forjs/?format=json').then(data =>{
  const circs = svg.selectAll('circle')
    .data(data);
  
  console.log(circs);
  
  circs.attr('cy', d => d.cy)
        .attr('cx', d => d.cx)
        .attr('r', d => d.r)
        .attr('cy', d => d.cy)
        .attr('fill', d => d.fill);
  console.log(circs);
  
  circs.enter()
    .append('circle')
      .attr('cx', d => d.cx)
      .attr('r', d => d.r)
      .attr('cy', d => d.cy)
      .attr('fill', d => d.fill);
  console.log(circs);
})
group.append('circle')
  .attr('r', 50)
  .attr('cx', 300)
  .attr('cy', 70)
  .attr('fill', 'pink');