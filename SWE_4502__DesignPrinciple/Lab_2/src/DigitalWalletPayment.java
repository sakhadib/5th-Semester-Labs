public class DigitalWalletPayment implements PaymentMethod{
    @Override
    public void pay(int dollars) {
        System.out.println("Paying " + dollars + " using Digital Wallet.");
    }
}
