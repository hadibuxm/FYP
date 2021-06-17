document.getElementById("countryname").value =  "{{countryname}}";
  if(!'{{topics}}')
  {
    if(!'{{seetweets}}' && !'{{fusedwords}}' && !'{{wordcount}}')
    {
      document.getElementById('seetweets').style.display= 'none'
      document.getElementById('fusedwords').style.display= 'none'
      document.getElementById('wordcount').style.display= 'none'
    }
    document.getElementById('selecttag').style.display = 'none'
    document.getElementById('trendheadline').style.display = 'none'
    document.getElementById('analysisbutton').style.display = 'none'
    
  }