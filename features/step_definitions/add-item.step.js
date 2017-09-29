var {defineSupportCode} = require('cucumber');
var assert = require('assert');

defineSupportCode(({Given, When, Then}) => {

  Given(/^I have an empty grocery list$/, function() {
    var groceryList = [];
    this.groceryList = groceryList;
  });

  When(/^I add an item to the list$/, function() {
    this.groceryList.push("item");
  });

  Then(/^The grocery list contains a single item$/, function() {
    assert.equal(this.groceryList.length, 1);
  });

  Then(/^I can access that item from the grocery list$/, function() {
    var foo = this.groceryList[0];
    assert.equal(foo, "item");

  });

  When(/^I add these items to the list:$/, function(table) {
    for (row of table.rows()) {
      this.groceryList.push(row[0]);
    }
  });

  Then('The length of the list is {int}', function(expectedSize) {
    assert.equal(this.groceryList.length, expectedSize);
  })

});