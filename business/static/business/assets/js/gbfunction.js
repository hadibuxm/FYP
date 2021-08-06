
/*document.getElementById("userid").style.display="none";
document.getElementById("description").style.display="none";
document.getElementById("followersmsg").style.display="none";
document.getElementById("lenofhashtagsmsg").style.display="none";
*/
/*
function display(){
  document.getElementById("userid").style.display="block";
  document.getElementById("description").style.display="block";
  document.getElementById("followersmsg").style.display="block";
  document.getElementById("lenofhashtagsmsg").style.display="block";
}*/
/*
if('{{script_message}}'=='yes'){
  display();
}
*/
function setoptions(brands, brands_id) {
  for (let i = 1; i <= brands.length; i++) {
          document.getElementById(i.toString()).innerHTML = brands[i-1];
          document.getElementById(i.toString()).value = brands_id[i-1];
        }
  if (brands.length != 10){
    for (let j = brands.length+1; j<=10; j++){
      document.getElementById(j).style.display = "none";
    }
  }
}

function hideselectionboxes(){
    document.getElementById("1").style.display= "none";
    document.getElementById("2").style.display= "none";
    document.getElementById("3").style.display= "none";
    document.getElementById("4").style.display= "none";
    document.getElementById("5").style.display= "none";
    document.getElementById("6").style.display= "none";
    document.getElementById("7").style.display= "none";
    document.getElementById("8").style.display= "none";
    document.getElementById("9").style.display= "none";
    document.getElementById("10").style.display= "none";
}

function showselectionboxes(){
    document.getElementById("1").style.display= "block";
    document.getElementById("2").style.display= "block";
    document.getElementById("3").style.display= "block";
    document.getElementById("4").style.display= "block";
    document.getElementById("5").style.display= "block";
    document.getElementById("6").style.display= "block";
    document.getElementById("7").style.display= "block";
    document.getElementById("8").style.display= "block";
    document.getElementById("9").style.display= "block";
    document.getElementById("10").style.display= "block";
}

// hide selectionboxes
hideselectionboxes();
function showbusinesses(){
    // get value of selected category
    var category = document.getElementById("selectcategory").value;
    switch(category){
      case "clothing":
        showselectionboxes(); // show selection boxes
        const clothing_brands = [
          "J. Junaid Jamshed" , "Gul Ahmed" , "Nishat Linen", "Bareeze" , "Khaadi" , "Kayseria", "KROSSKULTURE", "edenrobe", "OrientTextiles", "affordablepk"
        ];

        const clothing_brands_ids = [
          "@_JunaidJamshed" , "@GulahmedFashion" , "@nishatlinen","@BareezeOfficial" , "@KhaadiOfficial" , "@KayseriaPK", "@KrossKulturePk" , "@edenrobe_pk" , 
          "@OrientTextiles", "@affordablepk"
        ];
        setoptions(clothing_brands, clothing_brands_ids);
        break;

      case "foodonline":
        showselectionboxes(); // show selection boxes
        const food_brands = ["foodpanda" , "kfcpakistan" , "MENU", "Eat Mubarak" , "Supermeal Pakistan" , "K&N's Pakistan", "foodpakistan", 
          "foodnerd", "cheetay"
        ];

        const food_brands_ids = ["@foodpanda_pk" , "@kfc_pk" , "@Seasonsfoods", "@EatMubarak_Pk" , "@SupermealPK" , "@KandNs", 
          "@Foodpakistanpk" , "@Foodnerdpk" , "@cheetaypk"
        ];
        setoptions(food_brands, food_brands_ids);
        break;

      case "onlineshopping":
        showselectionboxes();
        const shopping_brands = [
          "Amazon", "AliExpress" , "HomeShopping", "iShoppingpk" , "Daraz" , "Alibaba" , "Elo" , "Telemart Official" , "Tejar.pk" , "Goto Online Shopping"
        ]; 

        const shopping_brands_id = [
          "@amazon" , "@AliExpress_EN" , "@homeshoppingpk" , "@iShoppingpk" , "@darazpk" , "@AlibabaB2B", "@ExportLeftovers" , "@Telemartstores",
          "@TejarPK" , "@GotocomPk"
        ];
        setoptions(shopping_brands , shopping_brands);
        break;
      case "mobilepayment":
        showselectionboxes(); // show selection boxes
        const mobilepayment = [
          "JazzCash" ,  "EasyPaisa" , "Zong PayMax" , "UBL Omni" , "Keenu Wallet" , "SimSim" , "UPaisa" 
        ];

        const mobilepayment_id = [
          "@JazzCash" , "@easypaisa" , "@Zongers" , "@UBLDigital" , "@KeenuPak" , "@FINCA_Pakistan" , 
          "@UpaisaOfficial"
        ];
        setoptions(mobilepayment, mobilepayment_id);
        break;
        
      case "footwear":
        showselectionboxes();
        const footwear = [
          "Stylo Shoes" , "Unze London (Pakistan)" , "Hush Puppies PK" , "Cat Footwear" , "Borjan Shoes" ,
          "Metro Shoes Pakistan" , "Bata Pakistan" , "Starlet Shoes"
        ];
        const footwear_id = [
          "@StyloShoesPK" , "@unzepakistan" , "@HushPuppiesPak" , "@CatFootwear" , "@borjanshoes1" ,
          "@MetroShoesbyNY" , "@BataPakistanLtd" , "@onlinestarlet"
        ] ;
        setoptions(footwear, footwear_id);
        break;

      case "property":
        showselectionboxes(); // show selection boxes
        const property = [
          "Bahria Town Official", "DHA", "Abdullah Group", "Habib Rafiq", "Ali Builders & Developers",
          "ZEM Builders", "Lahore Development Authority (LDA)."
        ]; 

        const property_id = [
          "@BahriaTownOffic", "@DHAToday", "@ABDBuilders", "@habibrafiqpvt", "@alibuilders", "@zembuilders", 
          "@LHRDevAuthority"
        ];
        setoptions(property, property_id);
        break;

      case "beverage":
        showselectionboxes(); // show selection boxes
        const beverage = [
          "Pakola Pakistan", "pepsipakistan", "Coca-Cola Pakistan", "Murree Brewery", "NESTLÉ PURE LIFE",
          "Mountain Dew", "Sprite", "Fanta", "7UP Pakistan", "Mirinda Pakistan"
        ];

        const beverage_id = [
          "@PakolaPakistan", "@pepsipakistan", "@CokePk", "@MurreeBrewery", "@PureLifePK", "@DewPK",
           "@Sprite", "@fantapakistan", "@7UP_PK", "@MirindaPK"
        ];
        setoptions(beverage, beverage_id);
        break;
      case "banks":
        showselectionboxes(); // show selection boxes
        const banks = [
          "SBP", "National Bank Of Pakistan NBP", "Sindh Bank Ltd", "Bank Of Khyber", 
          "First Women Bank Limited", "Askari Bank Limited", "Bank Alfalah", "MCB Bank Limited", 
          "The Bank of Punjab"
        ];
        const banks_id = [
          "@StateBank_Pak", "@nationalbankpk", "@SINDHBANKMEDIA", "@TheBankofKhyber", "@FWBLbank", 
          "@Askari_Bank", "@BankAlfalahPAK", "@MCBBankPk", "@thebankofpunjab"
        ];
        setoptions(banks, banks_id);
        break;

      case "mobileoperator":
        showselectionboxes(); // show selection boxes
        const mobileoperator = [
          "Telenor, Pakistan", "Jazz", "ufone", "Zong", "Warid Telecom" 
        ];
        const mobileoperator_id = [
          "@telenorpakistan", "@jazzpk", "@Ufone", "@Zongers", "@Waridpak"
        ];
        setoptions(mobileoperator, mobileoperator_id);
        break;

      case "automobiles":
        showselectionboxes(); // show selection boxes
        const automobiles = [
          "Toyota Pakistan", "Suzuki Pakistan", "Yamaha Motor Pakistan", "MG Motor Pakistan",
          "Honda Atlas Cars Pakistan Limited", "Kia Motors Pakistan", "Audi Pakistan", "JAGUAR PAKISTAN LTD.",
          "Lamborghini", "Mercedes-Benz"
        ];

        const automobiles_id = [
          "@ToyotaPak", "@SuzukiPakistan", "@YamahaMotorPk", "@MGPakistan", "@HACPLOfficial", "@KiaMotorsPK",
          "@AudiPakistan", "@Jaguarpakistan", "@Lamborghini", "@MercedesBenz"

        ];
        setoptions(automobiles, automobiles_id);
        break;
      
      case "technology":
        showselectionboxes(); // show selection boxes
        const technology = [
          "Microsoft", "Amazon Inc", "Alphabet Inc", "Tencent", "Facebook", "Alibaba Group", "Nvidia", "TSMC"
        ];
        const technology_id = [ 
          "@Microsoft", "@amazon", "@Alphabetlnc", "@TencentGlobal", "@Facebook", "@AlibabaGroup", "@nvidia",
          "@TSMCGlobal" 
        ];
        setoptions(technology, technology_id);
        break;

        default:
        hideselectionboxes(); // call function for hiding selection boxes
}}