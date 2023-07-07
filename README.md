# Trade-Backtest-Models
Name : Rohan Khanna
Email : 2020csb1117@iitrpr.ac.in
College : IIT Ropar

Assignment Details : (By Futures First)
To go through the following interest rate models. 
Vasicek Model
Cox-Ingersoll-Ross (CIR) Model
Heath-Jarrow-Morton (HJM) Model
Hull-White Model
1.Plot the forward curve using the above Models
2.Back test the model
3.To generate trading signals; How can we improve trading signals from the model. 
4.Why the model is different from the other model and How it is better than the other model.

So for each model, here a python file is given.
To run this code, please make sure : 
* You should have data for maturity and actual interest rate.
* Also, set column name to 'Maturity' and 'Rate'
* Now, set the name of data file to historical_data.csv
* Keep this data file in directory of code and then run code on your terminal.

Now, simply run file for any interest rate model. 
STEP 1 : Run python code using python [file_name].py
STEP 2 : You will see a predicted forward rate curve based on formula for that interest rate model.
STEP 3 : As soon as you will close the graph, you will see trading signals generated and it will predict on whether to BUY/SELL on all maturities.
STEP 4 : Also, backtesting results will be generated specifying Total Return, Annualized return, Portfolio Returns and Buy/Sell Efficiency.

In case of errors : 
Just check once that the date format of Maturity matches with the date format specified in code. It may be different in your case.

NOTE THAT : Data I used was confidential to Futures First, so you must have some actual data for running this simulation.
