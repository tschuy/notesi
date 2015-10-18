//
//  cameraViewController.h
//  Notesi
//
//  Created by Nawwaf Almutairi on 10/18/15.
//  Copyright (c) 2015 Nawwaf. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface cameraViewController : UIViewController

@property (strong, nonatomic) IBOutlet UIImageView *imageView;


- (IBAction)takePhoto:(UIButton *)sender;

- (IBAction)selectPhoto:(UIButton *)sender;

@end
@interface APPViewController : UIViewController <UIImagePickerControllerDelegate, UINavigationControllerDelegate>
@end
