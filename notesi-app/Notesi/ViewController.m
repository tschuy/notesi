//
//  ViewController.m
//  Notesi
//
//  Created by Nawwaf Almutairi on 10/17/15.
//  Copyright (c) 2015 Nawwaf. All rights reserved.
//

#import "ViewController.h"


@interface ViewController ()

@end


@implementation ViewController

#pragma mark -
#pragma mark NSURLConnection Delegate Methods

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    [self.passWord setDelegate:self];
    [self.userName setDelegate:self];
    


}

- (NSString *) getDataFrom:(NSString *)url{
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"GET"];
    [request setURL:[NSURL URLWithString:url]];
    
    NSError *error = [[NSError alloc] init];
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    if([responseCode statusCode] != 200){
        NSLog(@"Error getting %@, HTTP status code %i", url, [responseCode statusCode]);
        return nil;
    }
    
    return [[NSString alloc] initWithData:oResponseData encoding:NSUTF8StringEncoding];
}



- (IBAction)logIn:(id)sender {
    
    [self getDataFrom:@"dh.tschuy.com"];
    
}
-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender{
    
    if ([[segue identifier] isEqualToString:@"signInSegue"]) {
        [segue destinationViewController];
    }
}

-(BOOL) textFieldShouldReturn:(UITextField *)textField{
    
    [textField resignFirstResponder];
    return YES;
}



@end
