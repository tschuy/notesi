//
//  ViewController.h
//  Notesi
//
//  Created by Nawwaf Almutairi on 10/17/15.
//  Copyright (c) 2015 Nawwaf. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UITextField *userName;
@property (weak, nonatomic) IBOutlet UITextField *passWord;

@property (nonatomic, retain) NSData* responseData;


@end

