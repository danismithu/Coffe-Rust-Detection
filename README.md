# Coffee-Rust-Detection
## Description
This is a simple example of an image classifier made with Tensorflow MobilenetV2. This is used to detect if a coffee plant is either healthy or has a disease caused by a red spider mite or has rust level 1, 2, 3 or 4. In order to use the classifier you have to pay $0.75. Since this a project in progress it has a credit card for testing provided by Stripe, more of that below.

The application is mounted in a Render server. Go to this link in order to see the project https://coffee-rust-detection.onrender.com/

To pay for the service you can use the following information:
- Email: Any you want.
- Credit card number: 4242 4242 4242 4242
- Exp. date: Any date in the future.
- CVV: Any 3 or 4 numbers, for example 111

Once the payment is accepted you will be redirected to the page where the ML works. Add an image as the one below and click analyze. It will predict one of the five classes mentioned previously!

![Alt text](uploads/C1P1E2.jpg?raw=true "Coffee plant")

## References
The dataset was obtained from [here](https://data.mendeley.com/datasets/c5yvn32dzg/2)

## Future Work
The model should be retrained or changed since it has just about 49.36% of accuracy.
